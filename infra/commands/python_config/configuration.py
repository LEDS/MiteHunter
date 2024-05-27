import mysql.connector
import time
import os
import subprocess

def execute_sql_dump():
    # Comando que você deseja executar
    comando = "cat backup.sql | docker exec -i mysql /usr/bin/mysql -u root --password=12345 MiteHunter"

    # Executar o comando
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    # Verificar se a execução foi bem-sucedida
    if resultado.returncode == 0:
        # Imprimir a saída do comando
        print("Saída do comando:")
        print(resultado.stdout)
    else:
        # Imprimir mensagem de erro se a execução falhou
        print("Erro ao executar o comando.")


def databaseDump():    
    execute_sql_dump()


def try_connection():
    connection_config = {
        "host": os.environ['MYSQL_HOST'],
        "user": os.environ['MYSQL_USER'],
        "password": os.environ['MYSQL_PASSWORD'],
        "port": os.environ['MYSQL_PORT']
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
    databaseDump()
    budibase_ip_catch()
    databaseDump()

if __name__ == '__main__':
    budibase_ip_catch()