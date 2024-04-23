from django.db import models
from django.conf import settings
import os


# Create your models here.
class FormFile(models.Model):
    title = models.CharField(max_length=150)
    file  = models.FileField()
    cultivo_id = models.IntegerField()

    def save(self):
        file_name = os.path.join(settings.MEDIA_ROOT, self.title)

        with open(file_name, "wb") as f:
            for chunck in self.file.chunks():
                f.write(chunck)


    def __str__(self) -> str:
        return self.title