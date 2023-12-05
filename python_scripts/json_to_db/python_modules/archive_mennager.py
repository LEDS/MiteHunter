import json
import re
import _io
from os import rename, listdir
from typing import TextIO
from types import MethodType

# Caps variables mean constrains
AI_OUTPUT_PATH = "./json/ai_output"
CORRECT_DB_UPDATE_PATH = "./json/correct_db_update"
ERROR_DIR_PATH = "./json/error"
ENV_FILE_PATH = "./infra/.env"
YEAR_MONTH_DAY_PATTERN = r'^\d{4}-\d{2}-\d{2}$'


def move_file(file_name: str, file_folder_path: str, destination_folder_path: str, file_incremeant: str=""):
    """
    Feature: move a file to other folder

    @param file_name: name of the file you want to move
    @param file_folder_path: path where the file is now
    @param destination_folder_path: path where you want to send the file
    """

    old_name = f"{file_folder_path}/{file_name}"
    new_name = f"{destination_folder_path}/{file_incremeant}{file_name}"

    rename(old_name, new_name)


def get_all_json_file_names(json_files_path: str = AI_OUTPUT_PATH) -> list:
    """
    Feature: get all jsons in specific folder

    @param json_files_path: folder path where the jsons are stored

    @return: a list of all jsons name in specifc folder
    """

    all_files = [file for file in listdir(json_files_path) if file.endswith(".json")]
    return all_files


def get_json_data(json_path: str) -> list:
    """
    Feature: extract the data from json as list or dict Python type

    @param json_path: the path where json file is, included its name

    @return: return the json data information as list Python type
    """

    with open(json_path, "r") as f:
        json_data = json.load(f)

    return json_data


def read_file(path: str) -> str | None:
    """
    Feature: Try to get data from specifc file

    @param path: the path where file is storage 
    
    @return: the file data if file is found | None if file not found
    """

    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


def try_generate_error_log(my_sql_connector: MethodType, log_text: str):
    try:
        my_sql_connector(log_text)
    except Exception as e:
        print(e)


class JsonData:
    def __init__(self):
        self._json_data = TextIO()
        self._actual_line = ""
        self._actual_line_as_dict = None
        self._actual_line_dict_key = str()
        self._info_line = True

    def try_get_next_line(self) -> bool:
        try:
            next(self)
            return True
        except StopIteration:
            self._json_data.close()
            return False

    def actual_line_as_dict(self):
        self._actual_line_as_dict = dict()
        self._actual_line_dict_key = self.actual_line[self.actual_line.index('"')+1:self.actual_line.index(":")-1]
        values = self.actual_line[self.actual_line.index("[")+1:self.actual_line.index("]")].replace('"', "").replace(",", "").split()

        self._actual_line_as_dict[self._actual_line_dict_key] = values

    def check_json_data(self) -> bool:
        len_actual_line_as_dict = len(self._actual_line_as_dict[self._actual_line_dict_key])
        
        if len_actual_line_as_dict == 2 and self._info_line:
            sample_date, experiment_id = self._actual_line_as_dict[self._actual_line_dict_key]

            date_correct = bool(re.match(YEAR_MONTH_DAY_PATTERN, sample_date))
            id_correct = experiment_id.isnumeric()
            self._info_line = False

            return date_correct and id_correct
        
        elif len_actual_line_as_dict == 3:
            return True

        raise ValueError("Corrupted file")

    def try_update_line_dict_and_check_json_data(self) -> bool:
        try:
            self.actual_line_as_dict()
        except Exception:
            return False

        return self.check_json_data()

    @property
    def actual_line(self) -> str:
        return self._actual_line

    @actual_line.setter
    def actual_line(self, value: str):
        self._actual_line = value

    @property
    def json_data(self) -> TextIO:
        return self._json_data

    @json_data.setter
    def json_data(self, value: TextIO):
        self._json_data = value

    @property
    def actual_line_dict_values(self) -> list:
        return self._actual_line_as_dict[self._actual_line_dict_key]

    def __iter__(self):
        return self

    def __next__(self):
        self.actual_line = self.json_data.readline()
        while self.actual_line.startswith("{") or self.actual_line.startswith("}"):
            self.actual_line = self.json_data.readline()

        if not self.actual_line:
            raise StopIteration
