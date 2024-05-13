from django.conf import settings
import datetime
import os


def create_dir(c_id: int) -> str:
    date_today = datetime.date.today().strftime("%Y%m%d")
    directory = os.path.join(settings.MEDIA_ROOT, f"{str(c_id)}_{date_today}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return directory
    