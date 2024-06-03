import mysql.connector
import subprocess
import time
import os

def databaseDump():
    sql_file_path = os.environ['MYSQL_FILE']

    # Verifica se o arquivo existe
    if not os.path.exists(sql_file_path):
        print(f"Erro: O arquivo {sql_file_path} não existe.")
        return

    # Recupera a senha do MySQL a partir das variáveis de ambiente
    mysql_password = os.getenv('MYSQL_ROOT_PASSWORD')

    # Comando que você deseja executar
    command = f"cat {sql_file_path} | docker exec -i mysql /usr/bin/mysql -u root --password={mysql_password} MiteHunter"

    # Executa o comando e captura a saída
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    # Imprime a saída e erros, se houver
    print("stdout:", stdout)
    print("stderr:", stderr)


def try_connection():
    connection_config = {
        "host": os.environ['MYSQL_HOST'],
        "user": os.environ['MYSQL_USER'],
        "password": os.environ['MYSQL_PASSWORD'],
        "port": os.environ['MYSQL_PORT']
    }

    for c in range(12):
        try:
            return mysql.connector.connect(**connection_config)
        except mysql.connector.Error as e:
            print(f"ERROR: Failed to connect to database: {e}")
            print("Retrying in 1 minute...")
            time.sleep(30)
    return None


def budibase_ip_catch(connection):
    if connection is None:
        return

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM MiteHunter.BudibaseIpCatch")
        cursor.execute("INSERT INTO MiteHunter.BudibaseIpCatch (ip) VALUES (%s)", (os.environ['MYSQL_HOST'],))
        connection.commit()

    connection.close()


if __name__ == '__main__':
    connection = try_connection()
    databaseDump()
    budibase_ip_catch(connection)