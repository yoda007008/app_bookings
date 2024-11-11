from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
from pydantic import EmailStr
import os
from app.users.dao import UsersDAO
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, os.getenv("TOKEN"), os.getenv("ALGORITM")
    )
    return encode_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email = email)
    if not user and not verify_password(password, password):
        return None
    return user 
