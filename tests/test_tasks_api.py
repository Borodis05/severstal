def test_create_and_get_task(client):
    create_payload = {
        "title": "task-1",
        "description": "first",
        "status": "active",
    }
    create_resp = client.post("/tasks", json=create_payload)
    assert create_resp.status_code == 200
    data = create_resp.json()
    assert data["title"] == "task-1"
    assert data["description"] == "first"
    assert data["status"] == "active"
    assert "id" in data

    task_id = data["id"]
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == task_id


def test_list_tasks(client):
    client.post("/tasks", json={"title": "task-1", "description": None, "status": "active"})
    client.post("/tasks", json={"title": "task-2", "description": "d", "status": "completed"})

    resp = client.get("/tasks")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 2


def test_update_and_delete_task(client):
    create_resp = client.post("/tasks", json={"title": "task-1", "description": None, "status": "active"})
    task_id = create_resp.json()["id"]

    patch_resp = client.patch(f"/tasks/{task_id}", json={"status": "completed"})
    assert patch_resp.status_code == 200
    assert patch_resp.json()["status"] == "completed"

    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 204

    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
