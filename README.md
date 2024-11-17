# Приложение для бронирования отелей

## Краткое описание 

Это мой проект на фреимворке FastAPI. В API реализованна авторизация пользователей, настроенно подключение к реляционной базе данных и добавление в нее новых пользователей. Настроенно кэширование данных при помощи Redis, благодаря этому API работает быстрее. Также в этом проекте поработал над файлами cookie и JWT токенами.

## Технологии

Проект разработан с использованием следующего стека технологий:
- **FastAPI** — для создания API
- **SQLAlchemy** — ORM для работы с базой данных и тестирования SQL запросов
- **PostgreSQL** — реляционная база данных
- **Redis** — кэширование и поддержка очередей
- **Jinja** — шаблонизатор для генерации HTML
- **Alembic** — инструмент для управления миграциями
- **SQLAdmin** — создание админки

### Требования

- Python 3.8+
- PostgreSQL
- Redis
- Celery

## Структура проекта

```plaintext
app_bookings/
├── app/                      # Основной модуль проекта
│   ├── admin/                # Админка SQLAdmin
│   ├── bookings/             # Бронирования 
│   ├── dao/                  # Запросы к базе данных 
│   ├── images/               # Пример работы с изображениями в Celery
│   ├── migrations/           # Миграции Alembic
│   ├── pages/                # Запуск шаблона Jinja
│   ├── rooms/                # Комнаты
│   ├── static/               # Картинки
│   ├── tasks/                # Таски Celery 
│   ├── templates/            # Шаблоны Jinja
│   ├── users/                # Пользователи
│   ├── database.py           # Подключение базы данных
│   ├── exceptions.py         # Ошибки в отдельном файле (исправлено имя)
│   └── main.py               # Основное API
├── .env                      # Пример файла переменных окружения
├── requirements.txt          # Зависимости проекта
└── alembic.ini               # Краткая информация о миграциях

```

### Установка репозитория с проектом
```plaintext
    git clone https://github.com/yoda007008/app_bookings.git
```

Проект будет доступен по адресу: `http://127.0.0.1:8000/docs`
Админка SQLAdmin: `http://127.0.0.1:8000/docs`
