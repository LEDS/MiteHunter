from python_modules.mysql_features import MySQLJsonToDB
from python_modules.archive_mennager import JsonData, move_file, get_all_json_file_names, AI_OUTPUT_PATH, ERROR_DIR_PATH, CORRECT_DB_UPDATE_PATH, try_generate_error_log
from python_modules.error_notification_email_confidential import try_send_email

from schedule import every, repeat


my_sql = MySQLJsonToDB()
json_data = JsonData()


def in_error_cause(json_file: str):
    my_sql.get_execption_output()
    my_sql.update_error_index()
    my_sql.move_file_to_error_folder()
    my_sql.finish_db_connection()
    
    try_generate_error_log(my_sql.error_log_generator, f"The file {my_sql.json_name} had ben moved to {ERROR_DIR_PATH}")
    try_send_email(my_sql.error_log_text)
    json_data.json_data.close()
    move_file(json_file, AI_OUTPUT_PATH, ERROR_DIR_PATH, f"{my_sql.index_error}-")


def everything_ok_to_start() -> bool:
    """
    Feature: verify if can do the wanted insetrs. The inserts only can start if the json file has data to read and this data is correct
    
    @return: True if can; else False
    """

    return json_data.try_get_next_line() and json_data.try_update_line_dict_and_check_json_data()


def start_json_to_db_operation(json_file: str):
    """
    Feature: Executes all necessary modules to insert AI data into the DB
    """
    
    json_data.json_data = open(f"{AI_OUTPUT_PATH}/{json_file}", "r")  # load json data

    try:
        if everything_ok_to_start():  
            my_sql.json_name = json_file
            my_sql.sample_data = json_data.actual_line_dict_values
            
            while json_data.try_get_next_line():  # execute while exist sample data

                if json_data.try_update_line_dict_and_check_json_data(): #  execute while that data is correct
                    my_sql.mites_quantity = json_data.actual_line_dict_values
                    if my_sql.insert_amostra():
                        if not my_sql.insert_amostra_acaro():
                            raise Exception
                    else:
                        raise Exception
                else:
                    raise Exception
    
            move_file(json_file, AI_OUTPUT_PATH, CORRECT_DB_UPDATE_PATH)

    except Exception:
        in_error_cause(json_file=json_file)


@repeat(every(5).seconds)  # Chose cycle time
def job():
    """
    Feature: get and insert data from json AI output in DB every X time (5 seconds by defult)
    """
    
    if my_sql.try_make_db_connectio():
        jsons = get_all_json_file_names()  # list[str, str, ..., str] of jsons file names in AI_OUTPUT_PATH

        map(start_json_to_db_operation, jsons)
        
        my_sql.finish_db_connection()
    
    else:
        print("Error to make the DB connection")  #TODO: devoplement an exception for DB not connected cause

