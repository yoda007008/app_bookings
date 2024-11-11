from typing import Optional
from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel
from app.booking.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)

@app.get("/hotels/{hotel_id}")
async def hotels(
    location: str,
    hotel_id: int, 
    date_to: date, 
    date_from,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),
):
    return date_to, date_from, location




# запуск сервера (команда) uvicorn app.main:app --reload

