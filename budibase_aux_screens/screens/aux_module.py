from django.conf import settings
import mysql.connector
import datetime
import os

def create_dir(c_id: int, date) -> str:

    if date == "" or date is None:
        date_today = datetime.date.today().strftime("%Y%m%d")
        directory = os.path.join(settings.MEDIA_ROOT, f"{str(c_id)}_{date_today}")

    else:
        formated_date = date.split("-")
        formated_date = ''.join(formated_date)
        directory = os.path.join(settings.MEDIA_ROOT, f"{str(c_id)}_{formated_date}")

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return directory

def get_pics_qnt(c_id):
    connection = try_connection()
    
    if connection != None:
        cursor = connection.cursor()
        cursor.execute("SELECT area FROM Cultivo WHERE id = (%s)", (c_id,))

        result = cursor.fetchone()
        if result is None:
            qnt = "20 a cada 1000 m²"

        else:
            qnt = result[0]
            qnt = round((qnt)/50 + 0.5)    #regra de negócio, quantidade de plantas por area

        return qnt


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
            