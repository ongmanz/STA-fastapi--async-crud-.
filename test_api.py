import pytest
from httpx import AsyncClient
from main import app

# Add user
@pytest.mark.asyncio
async def test_create_user_async():
    # Define the payload for the POST request
    payload = {
        "name": "New user 01",
        "description": "Description of user 01",
    }

    # Make an asynchronous POST request using AsyncClient
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json=payload)
        # response = ac.post("/users/", json=payload)
    
    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json() == {"name": "New user 01", "description": "Description of user 01"}


@pytest.mark.asyncio
async def test_update_user_async():
    #Update user name and description
    user_id = 1
    name_new = "abc"
    desc_new = "desc new"
    # Pay load
    payload = {
        "name": name_new,
        "description": desc_new,
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put(f"/users/{user_id}", json=payload)
        
    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": name_new, "description": desc_new}

@pytest.mark.asyncio
async def test_delete_user_async():
    # Adding an item to the in-memory database
    user_id = 1

    # Make an asynchronous DELETE request to delete the item
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Get userid
        users = await ac.get("/users")
        print(users)
        # for user in users:
        #     if user.name == 'User 03':
        #         user_id = user.id
        #         break
        # Delete
        response = await ac.delete(f"/users/{user_id}")
    
    # # # Assert the response status code and content
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}