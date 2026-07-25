"""Tests for Build Anything API."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_status(client):
    resp = client.get("/api/status")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "uptime_seconds" in data


def test_create_and_list_items(client):
    # Create
    resp = client.post("/api/items", json={"title": "Test Item", "description": "A test"})
    assert resp.status_code == 201
    item = resp.json()
    assert item["title"] == "Test Item"
    assert item["description"] == "A test"
    item_id = item["id"]

    # List
    resp = client.get("/api/items")
    assert resp.status_code == 200
    items = resp.json()
    assert any(i["id"] == item_id for i in items)

    # Delete
    resp = client.delete(f"/api/items/{item_id}")
    assert resp.status_code == 200


def test_delete_nonexistent(client):
    resp = client.delete("/api/items/99999")
    assert resp.status_code == 404
