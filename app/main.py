from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional
from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel
from app.booking.router import router as router_bookings
from app.users.models import Users
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from sqladmin import Admin, ModelView

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from app.database import engine
from redis import asyncio as aioredis

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)

@app.on_event("startup")
def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")


app = FastAPI()
admin = Admin(app, engine)


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    

admin.add_view(UsersAdmin)

# запуск сервера (команда) uvicorn app.main:app --reload

