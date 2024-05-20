from django.conf import settings
import datetime
import os

def create_dir(c_id: int, date) -> str:
    if date == "":
        date_today = datetime.date.today().strftime("%Y%m%d")
        directory = os.path.join(settings.MEDIA_ROOT, f"{str(c_id)}_{date_today}")
    else:
        formated_date = date.split("-")
        formated_date = ''.join(formated_date)
        directory = os.path.join(settings.MEDIA_ROOT, f"{str(c_id)}_{formated_date}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return directory