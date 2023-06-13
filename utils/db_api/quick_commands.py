from sqlalchemy import sql
from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(id: int, category: str):
    user = User(id=id, category=category, wishes=True)
    await user.create()


async def update_wishes(id: int, wishes: bool):
    user = await User.get(id)
    await user.update(wishes=wishes).apply()


async def get_category(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user.category


