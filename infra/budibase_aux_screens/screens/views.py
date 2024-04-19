from modules.image_manager import download_image
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFieldForm

# Create your views here.
def main(request):
    print(request)
    upload_file(request)
    return render(request, 'main.html', {})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFieldForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()
            # download_image(request.FILES["file"], 0)
    
    else:
        form = UploadFieldForm()

        