import asyncio
from datetime import date
from fastapi import APIRouter, Depends
from app.booking.dao import BookingDAO
from app.booking.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],   
)

@router.get("")
@cache(expire=20)
async def get_bookings(user: Users = Depends(get_current_user)): # -> list[SBooking]:  
    await asyncio.sleep(1)
    return await BookingDAO.find_all(user_id=user.id)

@router.get("")
@cache(expire=20)
async def add_booking(
    user: Users = Depends(get_current_user), 
):
    await asyncio.sleep(2)
    await BookingDAO.add(user_id=user.id)

@router.post("")
async def add_booking(room_id: int, 
       date_from: date, date_to: date, 
       user: Users = Depends(get_current_user)
):
    await BookingDAO.add(user.id, room_id, date_from, date_to)
    



