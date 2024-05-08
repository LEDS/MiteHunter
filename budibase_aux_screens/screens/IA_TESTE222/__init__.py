import dotenv
import os

dotenv.load_dotenv()

JSONS_PATH = os.getenv("JSONS_PATH")
PROCESSED_JSONS_PATH = os.getenv("PROCESSED_JSONS_PATH")
ENV_FILE = os.getenv("ENV_FILE")
SAMPLE_ID_SQL_FILE = os.getenv("SAMPLE_ID_SQL_FILE")
INSERT_SAMPLE_SQL_FILE = os.getenv("INSERT_SAMPLE_SQL_FILE")
INSERT_FOLIOLO_SQL_FILE = os.getenv("INSERT_FOLIOLO_SQL_FILE")