from __init__ import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
import mysql


def read_sql_command(path: str):
    text: str
    
    with open(path, 'r') as f:
        text = f.read()
    
    return text


class MySQLConnector:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        self.cursor = self.connection.cursor()


if __name__ == "__main__":
    pass
    # print(read_sql_command("C:/Users/LEDS/Desktop/temp/MiteHunter/infra/budibase_aux_screens/modules/MySQL/select.sql"))