from typing import Optional
from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel
from app.booking.router import router as router_bookings
from app.users.router import router as router_users
from app.pages.router import router as router_pages
app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)

# запуск сервера (команда) uvicorn app.main:app --reload

