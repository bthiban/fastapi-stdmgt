import pytest


@pytest.mark.asyncio
async def test_list_students(async_client):
    response = await async_client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_post_student(async_client):
    payload = {
        "full_name": "Alice Johnson",
        "dob": "2005-09-01",
        "gender": "female",
        "address": "123 Main Street",
        "email": "alice@example.com",
        "phone": "1234567890",
        "enrollment_year": 2024,
    }

    response = await async_client.post("/students/", json=payload)
    assert response.status_code == 201
    data = response.json()

    assert data["full_name"] == payload["full_name"]
    assert data["email"] == payload["email"]
    assert data["is_deleted"] == 0
    assert data["status"] == "active"
    assert "id" in data


@pytest.mark.asyncio
async def test_update_student(async_client):
    # First, create a student to update
    create_payload = {
        "full_name": "John Doe",
        "dob": "2001-01-01",
        "gender": "male",
        "address": "123 Test St",
        "email": "john.doe@example.com",
        "phone": "123456789",
        "enrollment_year": 2022,
    }

    create_resp = await async_client.post("/students/", json=create_payload)
    assert create_resp.status_code == 201
    created_student = create_resp.json()
    student_id = created_student["id"]

    update_payload = {
        "enrollment_year": 2023,
    }

    response = await async_client.patch(f"/students/{student_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()

    print("RESPONSE:", response.status_code, response.text)

    assert data["id"] == student_id
    assert data["enrollment_year"] == 2023
