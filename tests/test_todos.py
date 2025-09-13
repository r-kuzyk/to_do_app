import pytest

@pytest.fixture
def token(client):
    client.post("/auth/register", json={
        "username": "roman",
        "email": "roman@example.com",
        "password": "secret"
    })
    res = client.post("/auth/login", data={
        "username": "roman",
        "password": "secret"
    })
    return res.json()["access_token"]


def auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def test_create_todo(client, token):
    response = client.post("/todos", json={
        "title": "Buy milk",
        "description": "2 liters"
    }, headers=auth_header(token))
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy milk"
    assert data["description"] == "2 liters"
    assert data["completed"] == False

def test_get_todos(client, token):
    response = client.get("/todos", headers=auth_header(token))
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert len(todos) >= 1

def test_update_todo(client, token):
    # First create
    create = client.post("/todos", json={"title": "Test", "description": "X"}, headers=auth_header(token))
    todo_id = create.json()["id"]

    # Then update
    response = client.put(f"/todos/{todo_id}", json={
        "title": "Updated",
        "description": "New",
        "completed": True
    }, headers=auth_header(token))
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated"
    assert data["completed"] == True

def test_delete_todo(client, token):
    create = client.post("/todos", json={"title": "DeleteMe"}, headers=auth_header(token))
    todo_id = create.json()["id"]

    response = client.delete(f"/todos/{todo_id}", headers=auth_header(token))
    assert response.status_code == 204

    get_deleted = client.get(f"/todos/{todo_id}", headers=auth_header(token))
    assert get_deleted.status_code == 404
