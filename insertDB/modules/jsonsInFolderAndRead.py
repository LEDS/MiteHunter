import json
import os
from modules.processAndInsertOnDatabase import *

def checkExistsFilesFolder():
    """
    Feature: Function responsible for checking whether a file exists in the designated folder.

    @params: None.

    @return: None.
        - If a file exists, the function to read the file is called
        - If there is no file, the program execution follows another cycle until a new file exists.
    """
    print("Verificando...")
    folder = "jsons/"

    if os.path.exists(folder) and os.path.isdir(folder):
        files_in_folder = os.listdir(folder)

        if files_in_folder:
            readJsonData()
        else:
            return
    else:
        return

def readJsonData():
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

    path = "jsons/"
    dirs = os.listdir(path)

    for file in dirs:
        source = f"jsons/{file}"
        try:
            json_data = None
            dest = f"jsonsProcessados/{file}"
            with open(f"jsons/{file}", "r") as f:
                json_data = json.load(f)
            informations = dictProcess(json_data)
            os.replace(source,dest)

            for value in informations:
                insertOnDatabase(value)
                
        except Exception as e:
            #dest = f"C:/Users/user/Desktop/MiteHunterIA/insertDB/jsonsErro/{file}"
            print(e)
            #os.replace(source,dest)