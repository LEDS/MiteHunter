from django.conf import settings
from django.shortcuts import render
from .aux_module import create_dir
from .models import FormFile

from IA.run_ia import run_ia

def main(request, c_id):
    return render(request, 'main.html', {'c_id': c_id})


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


def table_page(request, table_name: str):
    html_file: str = f"tables/{table_name}-table.html"

    return render(request, html_file, {})


def send_images(request, c_id: int):
    if request.method == 'POST':
        upload_files(request, c_id)

        run_ia()

        return render(request, 'close_window.html', {})

    return render(request, "send_images.html", {})