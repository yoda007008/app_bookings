import os
from fastapi import Depends, Request, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime
from app.users.dao import UsersDAO
from app.users.auth import *
from app.users.models import Users
from app.exeptions import TokenExpiredExeption, TokenAbsentException, EncorrectTokenFormatExeption, UserIsNotPresentException

def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try: 
        payload = jwt.decode(
            token, os.getenv("TOKEN"), os.getenv("ALGORITM")
        )
    except JWTError:
        raise EncorrectTokenFormatExeption
    
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredExeption
    
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    
    return user

