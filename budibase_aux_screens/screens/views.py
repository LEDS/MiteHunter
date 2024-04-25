from django.shortcuts import render
from .aux_module import create_dir
from .models import FormFile

def main(request, c_id):
    upload_files(request, c_id)
    return render(request, 'main.html', {})


def upload_files(request, c_id):
    if request.method == 'POST':
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
