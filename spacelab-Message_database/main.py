from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from models import User, Post
from utils import fill_database

app = FastAPI()

DATABASE_URL = "sqlite://./database.sqlite3"
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.on_event("startup")
async def on_startup():
    users_count = await User.all().count()
    if users_count == 0:
        await fill_database()

@app.get("/users/")
async def get_users():
    users = await User.all().prefetch_related("posts")
    return users

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first().prefetch_related("posts")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/user/{user_id}/posts/")
async def get_user_posts(user_id: int):
    user = await User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    posts = await Post.filter(user=user).all()
    return posts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
