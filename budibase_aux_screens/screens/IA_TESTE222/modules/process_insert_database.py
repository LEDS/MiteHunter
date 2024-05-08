from screens.IA_TESTE.modules.sample_elements import SampleTableElements
from screens.IA_TESTE.modules.mysql_connection import MySQL_Connection
from __init__ import ENV_FILE

def dict_process(ia_json: list, dict_sample_elements: dict) -> list:

    """
    Feature: Function responsible for processing the Json received so that all data contained in it is saved in a list where there is a dictionary containing the categories and their respective quantities.

    @param ia_json: List of dictionaries.

    @return: json_data[list]
         - json_data: returns a list of dictionaries, where the first key of the dictionaries is 'categorias', which has as an object a new dictionary with the categories as keys and their respective quantities as an object, the second key is 'cultivo_id', which has as object is the cultivation id, and the third key is 'data_Amos', which contains the date and the time the sample was taken.
    """
    """
    ia_json 
    json_data = 
    [
        ProcessedImage(user='fidelis@gmail.com_03042024_145758', 

        image=WindowsPath('images_processed/fidelis@gmail.com_03042024_145758/a-colony-of-two-spotted-spider-mites-tetranychus-urticae-adult-eggs-AH414C.jpg'), 

        counts=Counted(rajado=0, macropilis=0, californicus=0))
    ]

    json_data = [
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
    {'fidelis@gmail.com_13_03042024_145758': {'com_predador_com_rajado_percentage': 0.5, 'com_predador_sem_rajado_percentage': 0.5, 'classe_final': 'with_predator_with_mite', 'acao_sugerida': 'Não fazer nada!'}, 'wilsiman.evangelista.ifes@gmail.com_10_20240129_125740': {'um_a_cinco_rajado_percentage': 0.5, 'com_predador_com_rajado_percentage': 0.5, 'classe_final': 'one_to_five_mite', 'acao_sugerida': 'Jogar água!'}}
    """
    
    json_data = []
    for item in ia_json:
        # Abaixo é criado um outro dicionário dentro da key "foliolo" para armazenar as informações da tabela foliolo
        json_data.append({
            "foliolo": {}
            })
        for key, value in item.items():
            if key in ["data_Amos", "cultivo_id"]:
                json_data[-1][key] = value
                continue
            
            json_data[-1]["foliolo"][key] = value
    
        for file_name, counts in dict_sample_elements.items():
            for key, value in counts.items():
                json_data[-1][key] = value
    return json_data

def create_sample(insert_dict: dict):
    db = MySQL_Connection(ENV_FILE)

    response = db.insert_sample(insert_dict["data_Amos"], insert_dict["cultivo_id"], insert_dict["classe_final"], insert_dict["media_rajado_foliolo"], insert_dict["acao_sugerida"], insert_dict["qtd_total"], insert_dict["seis_a_nove_rajado_percentage"], insert_dict["mais_dez_rajado_percentage"], insert_dict["um_a_cinco_rajado_percentage"], insert_dict["sem_predador_sem_rajado_percentage"], insert_dict["com_predador_sem_rajado_percentage"], insert_dict["com_predador_com_rajado_percentage"])
    if not response.confirmation:
        print(f"ERROR IN INSERT IN TABLE 'Amostra'. ERROR CODE: {response.error}.")
        print(f"PARAMETERS USED: cultivo_id = {insert_dict['cultivo_id']}; date={insert_dict['data_Amos']}, classe_finalification={insert_dict["classe_final"]}, media_rajado_foliolo={insert_dict["media_rajado_foliolo"]}, acao_sugerida={insert_dict["acao_sugerida"]}, qtd_total={insert_dict["qtd_total"]}, six_to_nine_percentage={insert_dict["seis_a_nove_rajado_percentage"]}, moreThan_ten_percentage={insert_dict["mais_dez_rajado_percentage"]}, one_to_five_percentage={insert_dict["um_a_cinco_rajado_percentage"]}, sem_predador_sem_rajado_percentage={insert_dict["sem_predador_sem_rajado_percentage"]}, com_predador_sem_rajado_percentage={insert_dict["com_predador_sem_rajado_percentage"]}, com_predador_com_rajado_percentage={insert_dict["com_predador_com_rajado_percentage"]}")
        if response.msg_error is not None:
            print(f"MYSQL ERROR MESSAGE: {response.msg_error}")
        return


def insert_database(insert_dict: dict):

    """
    Feature: Function responsible for inserting the respective data into each table in the database.
         - Initially, the function calls the MySQL_Connection class, passing the environment file as a parameter to attempt to connect to the database.
         - If the connection is successful, the program continues with the insertion attempts.

    @param insert_dict: Dictionaries referring to each of the attributes of the database tables.

    @return: None.
        - If the insertion occurs without errors, the program prints the message "Data inserted correctly!"
        - If an error occurs in any part of the insertions, the program prints the error on the console.
    """

    db = MySQL_Connection(ENV_FILE)
        
    response = db.select_sample_id(insert_dict["data_Amos"], insert_dict["cultivo_id"])
    if not response.confirmation:
        print(f"ERROR IN SELECT ID IN TABLE 'Amostra'. ERROR CODE: {response.error}.")
        print(f"PARAMETERS USED: cultivo_id = {insert_dict['cultivo_id']}; date={insert_dict['data_Amos']}")
        if response.msg_error is not None:
            print(f"MYSQL ERROR MESSAGE: {response.msg_error}")
        return

    response = db.insert_leafs(*insert_dict["foliolo"].values(), response.data)
    if not response.confirmation:
        print(f"ERROR IN INSERT IN TABLE 'Foliolo'. ERROR CODE: {response.error}.")
        print(f"PARAMETERS USED: amostra_id={insert_dict['cultivo_id']}, category={'NULL'}, value={None}")
        if response.msg_error is not None:
            print(f"MYSQL ERROR MESSAGE: {response.msg_error}")
        return

    print("Data inserted correctly!")