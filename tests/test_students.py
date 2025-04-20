import pytest


@pytest.mark.asyncio
async def test_list_students(async_client):
    response = await async_client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
