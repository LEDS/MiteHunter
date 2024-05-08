from screens.IA_TESTE.modules.process_insert_database import *
from __init__ import JSONS_PATH, PROCESSED_JSONS_PATH
import json
import os


def check_exists_files_folder(dict_sample_elements):
    """
    Feature: Function responsible for checking whether a file exists in the designated folder.

    @params: None.

    @return: None.
        - If a file exists, the function to read the file is called
        - If there is no file, the program execution follows another cycle until a new file exists.
    """
    folder = JSONS_PATH

    if os.path.exists(folder) and os.path.isdir(folder):
        files_in_folder = os.listdir(folder)

        if files_in_folder:
            read_json_data(dict_sample_elements)
        else:
            return
    else:
        return

def read_json_data(dict_sample_elements):
    """
    Feature: Function responsible for reading data contained in a Json file.
        - When this function is called, it tries to read the file sent by the "checkExistsFilesFolder" function.
            - If the function can read the file, it is sent to the processaDict function and saves it in the information variable
                - After that, the file is moved to the jsonsProcessados folder
                - The information variable contains a list of dictionaries, through a "for", the dictionaries present in this list are sent to the insertOnDatabase function
            - If the function is unable to read the file, the error that occurred is printed on the console and the file is moved to the jsonsErro folder.

    @params: None.

    @return: None.
    """

    path = JSONS_PATH
    dirs = os.listdir(path)

    for file in dirs:
        source = f"{JSONS_PATH}/{file}"
        try:
            json_data = None
            dest = f"{PROCESSED_JSONS_PATH}/{file}"
            with open(f"{JSONS_PATH}/{file}", "r") as f:
                json_data = json.load(f)
            informations = dict_process(json_data, dict_sample_elements)
            os.replace(source,dest)

            create_sample(informations[0])

            for value in informations:
                insert_database(value)
                
        except Exception as e:
            print(f'O erro em readJsonData é: {e}')