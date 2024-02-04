from PIL import Image
import os
import datetime

def get_image_info(image_path) -> None:

    # Abra a imagem usando Pillow
    #image = Image.open(image_path)

    stat = os.stat(image_path)

    creation_time = stat.st_ctime
    creation_date = datetime.datetime.fromtimestamp(creation_time)

    date = creation_date.strftime("%d-%m-%Y")

    path = os.path.abspath(image_path)

    name = os.path.basename(path)


    return {"data": date, "name": name}