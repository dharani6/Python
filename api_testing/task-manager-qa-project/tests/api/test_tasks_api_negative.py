"""
Negative and boundary tests. In real interviews, this file is the one that
separates 'wrote some tests' from 'thinks like a QA engineer' -- it proves
you test failure paths and contracts, not just happy paths.
"""
import pytest
import requests


def test_create_task_without_title_returns_400(base_url):
    resp = requests.post(f"{base_url}/api/tasks", json={})
    assert resp.status_code == 400
    assert "error" in resp.json()


def test_create_task_with_blank_title_returns_400(base_url):
    resp = requests.post(f"{base_url}/api/tasks", json={"title": "   "})
    assert resp.status_code == 400


def test_get_nonexistent_task_returns_404(base_url):
    resp = requests.get(f"{base_url}/api/tasks/9999")
    assert resp.status_code == 404


def test_update_nonexistent_task_returns_404(base_url):
    resp = requests.put(f"{base_url}/api/tasks/9999", json={"title": "x"})
    assert resp.status_code == 404


def test_delete_nonexistent_task_returns_404(base_url):
    resp = requests.delete(f"{base_url}/api/tasks/9999")
    assert resp.status_code == 404


def test_update_task_with_blank_title_returns_400(base_url):
    created = requests.post(f"{base_url}/api/tasks", json={"title": "Keep me"}).json()
    resp = requests.put(f"{base_url}/api/tasks/{created['id']}", json={"title": "   "})
    assert resp.status_code == 400


@pytest.mark.parametrize("invalid_id", ["abc", "1.5", "-1"])
def test_non_integer_id_returns_404_not_500(base_url, invalid_id):
    resp = requests.get(f"{base_url}/api/tasks/{invalid_id}")
    assert resp.status_code == 404
