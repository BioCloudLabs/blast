import pytest
from app import app

@pytest.mark.asyncio
async def test_hello_world():
    response = await app.test_client().get('/')
    assert response.status_code == 200
    assert await response.get_json() == {'message': 'Hello, World!'}