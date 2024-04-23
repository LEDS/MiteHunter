from django.conf import settings
from django.shortcuts import render
from .models import FormFile
import datetime
import os

def main(request, c_id):
    upload_files(request, c_id)
    return render(request, 'main.html', {})


def upload_files(request, c_id):
    if request.method == 'POST':
        files = request.FILES.getlist("myfile")
        
        date_today = datetime.date.today().strftime("%Y%m%d")
        print(date_today)
        directory = os.path.join(settings.MEDIA_ROOT, f"{str(c_id)}_{date_today}")
        if not os.path.exists(directory):
            os.makedirs(directory)

        i = 0 
        for file in files:
            if ("image/" in file.content_type):
                file_extension = file.content_type[6:]
                form = FormFile(title=f"{str(c_id)}_{date_today}/imagem{i}.{file_extension}", file=file, cultivo_id=c_id)
                form.save()
                i+=1    
