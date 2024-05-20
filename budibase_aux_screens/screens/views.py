from django.shortcuts import render
from .aux_module import create_dir
from django.conf import settings
from .models import FormFile
import mysql.connector
import os

from IA.run_ia import run_ia

def main(request, c_id):
    if request.method == 'POST':
        upload_files(request, c_id)

        run_ia()

        return render(request, 'close_window.html', )
    
    qnt = "20 a cada 1000 m²"
    connection = try_connection()
    if connection != None:
        cursor = connection.cursor()
        cursor.execute("SELECT area FROM Cultivo WHERE id = (%s)", (c_id,))
        qnt = cursor.fetchone()[0]
        qnt = round((qnt)/50 + 0.5)    #regra de negócio, quantidade de plantas por area
    
    return render(request, 'main.html', {'qntPics': qnt})


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


def try_connection():
    connection_config = {
        "host": os.getenv("MYSQL_HOST"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "database": os.getenv("MYSQL_DATABASE"),
        "port": os.getenv("MYSQL_PORT")
    }

    try:
        return mysql.connector.connect(**connection_config)
    except mysql.connector.Error as e:
        print(f"ERROR: Failed to connect to database: {e}")
    return None
            