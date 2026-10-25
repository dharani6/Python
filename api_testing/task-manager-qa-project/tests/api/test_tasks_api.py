"""Positive-path API tests covering the full CRUD contract."""
import requests


def test_list_tasks_returns_empty_list_initially(base_url):
    resp = requests.get(f"{base_url}/api/tasks")
    assert resp.status_code == 200
    assert resp.json() == []


def test_create_task_returns_201_with_task_payload(base_url):
    resp = requests.post(f"{base_url}/api/tasks", json={"title": "Buy milk"})
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == "Buy milk"
    assert body["completed"] is False
    assert isinstance(body["id"], int)


def test_get_task_by_id_returns_correct_task(base_url):
    created = requests.post(f"{base_url}/api/tasks", json={"title": "Read book"}).json()
    resp = requests.get(f"{base_url}/api/tasks/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Read book"


def test_update_task_marks_it_completed(base_url):
    created = requests.post(f"{base_url}/api/tasks", json={"title": "Walk dog"}).json()
    resp = requests.put(f"{base_url}/api/tasks/{created['id']}", json={"completed": True})
    assert resp.status_code == 200
    assert resp.json()["completed"] is True


def test_update_task_can_change_title(base_url):
    created = requests.post(f"{base_url}/api/tasks", json={"title": "Old title"}).json()
    resp = requests.put(f"{base_url}/api/tasks/{created['id']}", json={"title": "New title"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "New title"


def test_delete_task_removes_it(base_url):
    created = requests.post(f"{base_url}/api/tasks", json={"title": "Temp task"}).json()
    resp = requests.delete(f"{base_url}/api/tasks/{created['id']}")
    assert resp.status_code == 204
    follow_up = requests.get(f"{base_url}/api/tasks/{created['id']}")
    assert follow_up.status_code == 404


def test_list_tasks_reflects_all_created_tasks_in_order(base_url):
    requests.post(f"{base_url}/api/tasks", json={"title": "A"})
    requests.post(f"{base_url}/api/tasks", json={"title": "B"})
    resp = requests.get(f"{base_url}/api/tasks")
    titles = [t["title"] for t in resp.json()]
    assert titles == ["A", "B"]
