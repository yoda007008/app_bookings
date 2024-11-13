from celery import Celery


# запуск celery 

celery = Celery(
    "tasks",
    broker="redis://localhost:6379",
    include=["app.tasks.tasks"]
)
