#!/usr/bin/env python
from __init__ import DB_NAME
import aiomysql
import asyncio
import time
import sys
import os

async def try_connection():
    connection_config = {
        "host": os.getenv("MYSQL_HOST"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "port": int(os.getenv("MYSQL_PORT"))
    }

    for c in range(5):
        try:
            return await aiomysql.connect(**connection_config)
        except aiomysql.Error as e:
            print(f"ERROR: Failed to connect to database: {e}")
            print("Retrying in 1 minute...")
            await asyncio.sleep(60)
    return None

async def budibase_ip_catch():
    connection = await try_connection()
    if connection is None:
        return

    async with connection.cursor() as cursor:
        await cursor.execute("DELETE FROM MiteHunter.BudibaseIpCatch")
        await cursor.execute("INSERT INTO MiteHunter.BudibaseIpCatch (ip) VALUES (%s)", (os.getenv("MYSQL_HOST"),))
        await connection.commit()

    connection.close()

async def async_code():
    await budibase_ip_catch()

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

    asyncio.run(async_code())
    execute_from_command_line(sys.argv)