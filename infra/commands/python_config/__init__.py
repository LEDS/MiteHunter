import dotenv
import os

dotenv.load_dotenv()

DB_NAME = os.getenv('MYSQL_DATABASE')
DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
DB_HOST = os.getenv('MYSQL_HOST')
DB_PORT = os.getenv('MYSQL_PORT')

JSONS_PATH = os.getenv("JSONS_PATH")
PROCESSED_JSONS_PATH = os.getenv("PROCESSED_JSONS_PATH")
ENV_FILE = os.getenv("ENV_FILE")
SAMPLE_ID_SQL_FILE = os.getenv("SAMPLE_ID_SQL_FILE")
INSERT_SAMPLE_SQL_FILE = os.getenv("INSERT_SAMPLE_SQL_FILE")
INSERT_FOLIOLO_SQL_FILE = os.getenv("INSERT_FOLIOLO_SQL_FILE")

