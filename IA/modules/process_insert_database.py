from modules.sample_elements import SampleTableElements
from modules.mysql_connection import MySQL_Connection

def dictProcess(iaJson: list) -> list:

    """
    Feature: Function responsible for processing the Json received so that all data contained in it is saved in a list where there is a dictionary containing the categories and their respective quantities.

    @param iaJson: List of dictionaries.

    @return: jsonData[list]
         - jsonData: returns a list of dictionaries, where the first key of the dictionaries is 'categorias', which has as an object a new dictionary with the categories as keys and their respective quantities as an object, the second key is 'cultivo_id', which has as object is the cultivation id, and the third key is 'data_Amos', which contains the date and the time the sample was taken.
    """
    """
    iaJson 
    jsonData = 
    [
        ProcessedImage(user='fidelis@gmail.com_03042024_145758', 

        image=WindowsPath('images_processed/fidelis@gmail.com_03042024_145758/a-colony-of-two-spotted-spider-mites-tetranychus-urticae-adult-eggs-AH414C.jpg'), 

        counts=Counted(rajado=0, macropilis=0, californicus=0))
    ]

    jsonData = [
    {
        'foliolo':
            {'imgOrig': 'img',
            'imgProc': 'imgP',
            'rajado': 10, 
            'macropilis': 5, 
            'californicus': 2},
            'cultivo_id': 13, 
            'data_Amos': '2023-10-25'
    }]
    {'fidelis@gmail.com_13_03042024_145758': {'with_predator_with_mite_percentage': 0.5, 'with_predator_without_mite_percentage': 0.5, 'final_class': 'with_predator_with_mite', 'suggested_action': 'Não fazer nada!'}, 'wilsiman.evangelista.ifes@gmail.com_10_20240129_125740': {'one_to_five_mite_percentage': 0.5, 'with_predator_with_mite_percentage': 0.5, 'final_class': 'one_to_five_mite', 'suggested_action': 'Jogar água!'}}
    """
    
    jsonData = []
    for item in iaJson:
        # MAGIA 1: cria um outro dicionário dentro da key "foliolo" para armazenar as informações da tabela foliolo
        jsonData.append({
            "foliolo": {}
            })
        for key, value in item.items():
            if key in ["data_Amos", "cultivo_id"]:
                jsonData[-1][key] = value
                continue
            
            jsonData[-1]["foliolo"][key] = value
    insert_data_dict(jsonData)

def insert_data_dict(jsonData: list[dict]):
    sample_table = SampleTableElements()
    for file_name, counts in sample_table.file_count_dict.items():
        for key, value in counts.items():
            jsonData[-1][key] = value
    return jsonData

def insertOnDatabase(insert_dict: dict):

    """
    Feature: Function responsible for inserting the respective data into each table in the database.
         - Initially, the function calls the MySQL_Connection class, passing the environment file as a parameter to attempt to connect to the database.
         - If the connection is successful, the program continues with the insertion attempts.

    @param insert_dict: Dictionaries referring to each of the attributes of the database tables.

    @return: None.
        - If the insertion occurs without errors, the program prints the message "Data inserted correctly!"
        - If an error occurs in any part of the insertions, the program prints the error on the console.
    """

    db = MySQL_Connection("C:/Users/wilsi/Desktop/MiteHunterSystem/MiteHunterSystem/.env")

    response = db.insert_amostra(insert_dict["data_Amos"], insert_dict["cultivo_id"], insert_dict["classificacao_final"], insert_dict["media_rajado_foliolo"], insert_dict["acao_sugerida"], insert_dict["qtd_total"], insert_dict["seis_a_nove"], insert_dict["mais_dez"], insert_dict["um_a_cinco"], insert_dict["sem_predador_rajado"], insert_dict["predador_sem_rajado"], insert_dict["com_predador_rajado"])
    if not response.confirmation:
        print(f"ERROR IN INSERT IN TABLE 'Amostra'. ERROR CODE: {response.error}.")
        print(f"PARAMETERS USED: cultivo_id = {insert_dict['cultivo_id']}; date={insert_dict['data_Amos']}")
        if response.msg_error is not None:
            print(f"MYSQL ERROR MESSAGE: {response.msg_error}")
        return
        
    response = db.select_idAmostra(insert_dict["data_Amos"], insert_dict["cultivo_id"])
    if not response.confirmation:
        print(f"ERROR IN INSERT IN TABLE 'Amostra'. ERROR CODE: {response.error}.")
        print(f"PARAMETERS USED: cultivo_id = {insert_dict['cultivo_id']}; date={insert_dict['data_Amos']}")
        if response.msg_error is not None:
            print(f"MYSQL ERROR MESSAGE: {response.msg_error}")
        return

    response = db.insert_foliolos(*insert_dict["foliolo"].values(), insert_dict["cultivo_id"])
    if not response.confirmation:
        print(f"ERROR IN INSERT IN TABLE 'Foliolo'. ERROR CODE: {response.error}.")
        print(f"PARAMETERS USED: amostra_id={insert_dict['cultivo_id']}, category={'NULL'}, value={None}")
        if response.msg_error is not None:
            print(f"MYSQL ERROR MESSAGE: {response.msg_error}")
        return

    print("Data inserted correctly!")