from fastapi import HTTPException, status

UserAlreadyExists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Пользователь уже существует"
)

IncorrectEmailPassword = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Неверная почта или пароль"
)

TokenExpiredExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Токен истек"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует"
)

EncorrectTokenFormatExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена"
)

UserIsNotPresentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

'''
RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не осталось свободных номеров"
) 
'''

# ошибка, которая закоментированна, применяется при заполненнном поле в базе данных