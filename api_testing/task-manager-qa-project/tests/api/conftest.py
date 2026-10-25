"""
Spins up a *real* Flask server in a background thread for the whole test
session, so tests hit it over real HTTP via `requests` -- the same way a
QA engineer would test any deployed REST service, not via Flask's internal
test client. This makes the suite portable: point `base_url` at a staging
URL and the same tests work unchanged.
"""
import os
import socket
import sys
import threading
import time

import pytest
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app import create_app


def _find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="session")
def base_url():
    port = _find_free_port()
    app = create_app()
    thread = threading.Thread(
        target=lambda: app.run(host="127.0.0.1", port=port, use_reloader=False),
        daemon=True,
    )
    thread.start()
    url = f"http://127.0.0.1:{port}"

    for _ in range(50):
        try:
            requests.get(url + "/api/tasks", timeout=0.5)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(0.1)
    else:
        raise RuntimeError("Flask test server did not start in time")

    yield url


@pytest.fixture(autouse=True)
def reset_tasks(base_url):
    """Every test starts from a clean, known state -- no test order coupling."""
    requests.post(f"{base_url}/api/tasks/reset")
    yield
