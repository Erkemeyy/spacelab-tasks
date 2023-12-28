from models import User, Post
import httpx

async def fetch_users_from_api():
    url = "https://gorest.co.in/public-api/users"
    response = await httpx.get(url)
    response_data = response.json()
    return response_data.get('data', [])


async def fill_database():
    users_data = await fetch_users_from_api()
    for user_data in users_data:
        user = await User.create(name=user_data['name'])
