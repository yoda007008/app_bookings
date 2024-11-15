from sqladmin import ModelView

from app.hotels.models import Hotels
from app.rooms.models import Rooms
from app.users.models import Users
from app.booking.models import Bookings

class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"

class BookingsAdmin(ModelView, model=Users):
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.room_id]
    name = "Бронь"
    name_plural = "Брони"
    

class HotelsAdmin(ModelView, model=Users):
    column_list = [c.name for c in Hotels.__table__.c] + [Hotels.room_quantity]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"



    