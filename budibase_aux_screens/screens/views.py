from django.shortcuts import render
from .aux_module import create_dir, get_pics_qnt
from django.conf import settings
from IA.run_ia import run_ia
from .models import FormFile
import os


TABLES_LIST: tuple[str] = (
    "Agricultor",
    "Propriedade",
    "Talhão",
    "Cultivo",
    "Consultar",
    "Cultivar",
    "Produtos",
    )


def main(request, c_id):
    if request.method == 'POST':
        sampleDir = upload_files(request, c_id)
        run_ia()                
        return render(request, 'close_window.html', {'cod_sample':os.path.basename(sampleDir)})
    
    qnt = get_pics_qnt(c_id)
    return render(request, 'send_images.html', {'qntPics': qnt, 'c_id': c_id})


def images_view(request, cod_sample):
    imgDir = os.path.join(settings.MEDIA_PATH, cod_sample)
    imgNames = [f for f in os.listdir(imgDir) if os.path.isfile(os.path.join(imgDir, f))]
    imgNames.sort()

    for i in range(len(imgNames)):
        imgNames[i] = os.path.join('media', (os.path.basename(cod_sample)), imgNames[i])
    
    return render(request, 'show_images.html', {'files':imgNames})


def tables(request, table_name: str):
    return render(request, f'screens/tables/{table_name.lower()}-table.html', {'tables_list': TABLES_LIST})


def upload_files(request, c_id):
    files = request.FILES.getlist("myfile")
    date = request.POST.get("date")
    directory = create_dir(c_id, date)

    i = 0 
    for file in files:
        if ("image/" in file.content_type):
            file_extension = file.content_type[6:]
            file_name = f"{directory}/imagem{i}.{file_extension}"
            
            form = FormFile(title=file_name, file=file)
            form.save()
            i+=1 
    return directory


def send_images_page(request, c_id):
    qnt = get_pics_qnt(c_id)
    return render(request, 'send_images.html', {'qntPics': qnt, 'c_id': c_id})