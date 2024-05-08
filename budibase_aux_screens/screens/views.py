from django.conf import settings
from django.shortcuts import render
from .aux_module import create_dir
from .models import FormFile
import sys
import os
mitehunter_path = os.path.join(settings.BASE_DIR, '..', settings.IA_PATH)
sys.path.append(mitehunter_path)
from IA.run_ia import run_ia

def main(request, c_id):
    if request.method == 'POST':
        upload_files(request, c_id)

        mitehunter_path = os.path.join(settings.BASE_DIR, '..', settings.IA_PATH)
        sys.path.append(mitehunter_path)
        from IA.run_ia import run_ia

        run_ia()

        return render(request, 'close_window.html', )

    return render(request, 'main.html', {})


def upload_files(request, c_id):
    files = request.FILES.getlist("myfile")
    directory = create_dir(c_id=c_id)

    i = 0 
    for file in files:
        if ("image/" in file.content_type):
            file_extension = file.content_type[6:]
            file_name = f"{directory}/imagem{i}.{file_extension}"
            
            form = FormFile(title=file_name, file=file)
            form.save()
            i+=1    

            