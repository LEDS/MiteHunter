# Feature:
# This module is responsible for storing the function that will be executed from time to time in main.py main function

# Own modules
from json_todb.python_modules.mysql_connection import MySQLConnection
from json_todb.python_modules.archive_mennager import get_json_data, get_all_json_file_names, ENV_FILE_PATH, AI_OUTPUT_PATH

# External modules
from schedule import every, repeat


mysql_connector = MySQLConnection(ENV_FILE_PATH)

@repeat(every(5).seconds)
def job():
    """
    Feature: verify if exist jsons in ai_output directory and, if exist, execute MySQLConnection.json_to_db_flow for each json file
    """
    
    jsons = get_all_json_file_names(AI_OUTPUT_PATH)

    for json in jsons:
        json_data = get_json_data(f"{AI_OUTPUT_PATH}/{json}")
        mite_id = (1, 2, 3)  # 1 = spider mite; 2 = predator mite; 3 = generic predator mite

        date_amt, amt_id = json_data["info"]
        mite_quantity = json_data["amostra"]

        mysql_connector.json_to_db_flow(amt_id, date_amt, json, mite_id, mite_quantity)

