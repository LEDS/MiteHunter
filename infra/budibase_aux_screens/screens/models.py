from django.db import models
from django.conf import settings
import os

class FormFile(models.Model):
    title = models.CharField(max_length=150)
    file  = models.FileField()
    cultivo_id = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        file_name = os.path.join(settings.MEDIA_ROOT, self.title)

        with open(file_name, "wb") as f:
            for chunk in self.file.chunks():
                f.write(chunk)

    def __str__(self) -> str:
        return self.title


class Imagem(models.Model):
    arquivo = models.ImageField(upload_to='imagens/')