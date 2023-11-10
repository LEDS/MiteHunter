# Feature:
# This module is responsible for storing important variables for paths, file directories and file management functions.

# Own modules
from json_todb.python_modules.error_notification_email_confidential import send_email  # switch: error_notification_email

# External modules
import json
from os import rename, listdir
from datetime import datetime
from types import NoneType

# Important variables for readability
# Caps variables mean constrains
ERROR_DIR_PATH = "json/error" 
AI_OUTPUT_PATH = "json/ai_output"
CORRECT_DB_UPDATE_PATH = "json/correct_db_update"
ENV_FILE_PATH = "infra/.env"

ERROR_LOG_TEMPLATE = """Error Code: {};
Function Arising: {};
Changes Made: {};
Error Date: {};
error time: {}"""  # This is a template to error log text


# Important Functions
def move_file(file_name: str, file_path: str, destination_path: str):
    """
    Feature: can move a file to other folder

    @param file_name: name of the file you want to move
    @param file_path: path where the file is now
    @param destination_path: path where you want to send the file
    """

    old_name = f"{file_path}/{file_name}"
    new_name = f"{destination_path}/{file_name}"

    rename(old_name, new_name)


def get_all_json_file_names(json_file_path: str) -> list:
    """
    Feature: get all jsons in specific folder

    @param json_file_path: folder path where the jsons are stored

    @return: a list of all jsons name in specifc folder
    """

    all_files = listdir(json_file_path)
    jsons_file = [file for file in all_files if file.endswith(".json")]
    return jsons_file


def get_json_data(file_path: str) -> list:
    """
    Feature: extract the data from json as list or dict Python type

    @param file_path: the path where json file is, included it's name

    @return: return the json data information as list Python type
    """

    with open(file_path, "r") as f:
        json_data = json.load(f)

    return json_data


def error_index(path: str = ERROR_DIR_PATH) -> int:
    """
    Feature: get all error logs in error directory to return the next error index

    @param path: path where error log are

    @return: next error index
    """

    last_error_log = listdir(path)[-1]
    index_error_separator = last_error_log.index("-")
    last_index = last_error_log[:index_error_separator]

    return int(last_index) + 1


def error_log_generator(error_code: str, function_arising: str, changes: str, index_error: int):
    """
    Feature: Generates an error log in a specific folder

    @param error_code: generic and specifc error code that mysql_connection.py main class return
    @param function_arising: name of the function that can't be executed correctly, line and file
    @param changes: all changes mades during excecution
    @param index_error: the index of this specifc error
    """

    today = datetime.today()
    error_date = f"{today.day}-{today.month}-{today.year}"
    error_time = f"{today.hour}:{today.min}"

    file_name = f"{index_error}-errorLog"

    error_text = ERROR_LOG_TEMPLATE.format(
                                            error_code,
                                            function_arising,
                                            changes,
                                            error_date,
                                            error_time
    )

    with open(f"{ERROR_DIR_PATH}/{file_name}.txt", "w") as file:
        file.write(error_text)

        send_email(error_text)


def read_file(path: str) -> str | NoneType:
    """
    Feature: Try to get data from specifc file

    @param path: the path where file is storage 
    
    @return: the file data if file file is found | None if file not found
    """

    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

