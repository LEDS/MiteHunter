#!/usr/bin/env python
from __init__ import DB_NAME
import mysql.connector
import time
import sys
import os


def try_connection():
    connection_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
            "port": os.getenv("MYSQL_PORT")
        }
        
    while (True):
        try:
            return mysql.connector.connect(**connection_config)
        except mysql.connector.Error as e:
            print(f"ERROR: Failed to connect to database: {e}")
            print("Retrying in 1 minute...")
            time.sleep(60)


def budibase_ip_cath():
        connection = try_connection()
        cursor =  connection.cursor()
        params = [os.getenv("MYSQL_HOST")]
        
        cursor.execute("DELETE FROM BudibaseIpCatch")
        cursor.execute("INSERT INTO BudibaseIpCatch (ip) VALUES (%s)", params = params)
        connection.commit()
        cursor.close()
        connection.close()
        

def manage():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budibase_aux_screens.budibase_aux_screens.settings')

    # Adiciona o diretório raiz do projeto ao PYTHONPATH
    root_project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(root_project_path)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    budibase_ip_cath()
    execute_from_command_line(sys.argv)
