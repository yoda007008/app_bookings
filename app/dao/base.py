from sqlalchemy import insert, select
from app.database import async_session_maker
from app.booking.models import Bookings
from app.users.models import Users


class BaseDAO: 
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(Bookings).filter_by(**filter_by)
            bookings = await session.execute(query)
            return bookings.scalars().all()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_user_by_id(user_id: int):
        async with async_session_maker as session:
            result = await session.execute(select(Users).where(Users.id == int(user_id)))
            user = result.scalars().first()
        return user
            