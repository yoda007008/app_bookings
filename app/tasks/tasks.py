from app.tasks.celery import celery
from PIL import Image
from pathlib import Path 

# пример celery task
'''
@celery.task
def process_pic( 
    path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resizzed_1000_500 = im.resize((1000, 500))
    im_resizzed_200_100 = im.resize((200, 100))
    im_resizzed_1000_500.save(f"app/static/resizzed_1000_500_{im_path.name}")
    im_resizzed_200_100.save(f"app/static/resizzed_200_100_{im_path.name}")
'''