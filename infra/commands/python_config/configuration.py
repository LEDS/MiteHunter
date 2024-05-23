import mysql.connector
import time
import os

def try_connection():
    connection_config = {
        "host": os.getenv('MYSQL_HOST'),
        "user": os.getenv('MYSQL_USER'),
        "password": os.getenv('MYSQL_PASSWORD'),
        "port": os.getenv('MYSQL_PORT')
    }

    for c in range(5):
        try:
            return mysql.connector.connect(**connection_config)
        except mysql.connector.Error as e:
            print(f"ERROR: Failed to connect to database: {e}")
            print("Retrying in 1 minute...")
            time.sleep(60)
    return None

def budibase_ip_catch():
    connection = try_connection()
    if connection is None:
        return

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM MiteHunter.BudibaseIpCatch")
        cursor.execute("INSERT INTO MiteHunter.BudibaseIpCatch (ip) VALUES (%s)", (os.getenv('MYSQL_HOST'),))
        connection.commit()

    connection.close()

def main():
    budibase_ip_catch()

if __name__ == '__main__':
    budibase_ip_catch()