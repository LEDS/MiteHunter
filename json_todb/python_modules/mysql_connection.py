# Feature:
# This module is responsible for storing a class that connects Python to the DB and inserts and retrieves information from them

# Own modules
from json_todb.python_modules.error import ErrorHandling, get_execption_output
from json_todb.python_modules.archive_mennager import move_file, read_file, CORRECT_DB_UPDATE_PATH, AI_OUTPUT_PATH

# External modules
import mysql.connector
import os
from dotenv import load_dotenv


class MySQLConnection(ErrorHandling):  # todo: connection_config need pull info from .env archive
    def __init__(self, env_file_path: str):
        ErrorHandling.__init__(self)
        self.env_file = read_file(env_file_path)

    def generic_insert_into_table(self, table_name: str, columns_name: tuple, values: tuple) -> tuple[str, Exception, str] | str:
        """
        Feature: insert data in specifc table

        @param table_name: name of table that you want to insert values
        @param columns_name: a tuple that contains each column name from your table, except id
        @param values: a tuple that conatins each value you want to insert

        @return:
            Error case:
                the string contains a generic error, that could be Connection not established or Error executing SQL
                the exception contais the specifc error, that could be any error class from mysql.connector
                the string contains the execption output
            Success case:
                the string contais the folow message: Success
        """

        param_names_handling = str(columns_name).replace("'", "")
        values_assist = "%s," * len(values)

        sql_code = f"INSERT INTO {table_name} {param_names_handling} VALUES ({values_assist[:-1]})"

        try:
            connection = mysql.connector.connect(**self.conection_config())
            cursor = connection.cursor(buffered=True)
        except Exception as e:
            return "Connection not established", e, get_execption_output()

        try:
            cursor.execute(sql_code, values)
            connection.commit()
        except Exception as e:
            connection.close()
            return "Error executing SQL", e, get_execption_output()

        cursor.close()
        connection.close()

        return "Success"

    def generic_get_info(self, table_name: str, column_want: str, where: bool = False, columns_filter: tuple = (), filter_values: tuple = ()) -> tuple[str, Exception, str] | list:
        """
        Feature: get data from specifc table

        @param table_name: name of table that you want to get value
        @param column_want: name of column you want get value
        @param where: use WHERE command in mysql to filter the results 
        @param columns_filter: used only if (where == True), a tuple that contains each column name that you want to filter
        @param filter_values: used only if (where == True), a tuple that conatins each value you want to filter in column

        ATTENTION THE PARAMETERS columns_filter AND filter_values MUST HAVE THE SAME LENGTH

        @return:
            Error case:
                the string contains a generic error, that could be Connection not established or Error executing SQL
                the exception contais the specifc error, that could be any error class from mysql.connector
                the string contains the execption output
            Success case:
                the string contais the folow message: Success
        """
        
        if where:
            filter_text = ("{} = %s AND " * len(columns_filter)).format(*columns_filter)[:-5]
            sql_code = f"SELECT {column_want} FROM {table_name} WHERE {filter_text}"
        else:  # No filter
            sql_code = f"SELECT {column_want} FROM {table_name}"

        try:
            connection = mysql.connector.connect(**self.conection_config())
            cursor = connection.cursor(buffered=True)
        except Exception as e:
            return "Connection not established", e, get_execption_output()

        try:
            if where:
                cursor.execute(sql_code, filter_values)
            else:  # No filter
                cursor.execute(sql_code)

            output = cursor.fetchall()

        except Exception as e:
            connection.close()
            return "Error executing SQL", e, get_execption_output()

        cursor.close()
        connection.close()

        return output

    def insert_amostra(self, experimento_id: int, data_amostra: str, json_name: str) -> bool:  # data_amostra should be like "year-month-day"
        """
        Feature: insert past values into the Amostra table and handle possible errors

        @param experimento_id: experience id is an important value to our database; it's get from ai json output
        @param data_amostra: sample data is an important value to our database; it's get from ai json output
        @param json_name: the name of json had ben data extract; if the function not work correctly, he must be exposed in errorlog 

        @return: if successful execute returns True, else returns False
        """

        output = self.generic_insert_into_table("Amostra", ("experimento_id", "data_amostra"), (experimento_id, data_amostra))

        if output != "Success":
            function_arising = "insert_amostra," + output[2]
            self.error_insert_amostra(output, function_arising, json_name)
            return False

        return True

    def get_id_amostra(self, experimento_id: int, data_amostra: str, json_name: str):
        """
        Feature: get id from Amostra table and handle possible errors

        @param experimento_id: experience id is an important value to our database; it's get from ai json output
        @param data_amostra: sample data is an important value to our database; it's get from ai json output
        @param json_name: the name of json had ben data extract; if the function not work correctly, he must be exposed in errorlog 

        @return: if successful execute returns True, else returns False
        """

        output = self.generic_get_info("Amostra", "id", True, ("experimento_id", "data_amostra"), (experimento_id, data_amostra))

        amostra_id = output[0][0] if len(output) > 0 else -1

        if amostra_id == -1:
            function_arising = "get_id_amostra," + output[2]
            self.error_get_id_amostra(output, function_arising, json_name)

        return amostra_id

    def insert_amostra_acaro(self, acaro_id: int, id_amostra: int, qtd: int, json_name: str) -> bool:
        """
        Feature: insert past values into the AmostraAcaro table and handle possible errors

        @param acaro_id: mite id is an important value to our database; id 1 mean spider mite, id 2 mean predator mite and id 3 mean generic predeator mite 
        @param id_amostra: sample id is an important value to our database; it's get from get_id_amostra output
        @param json_name: the name of json had ben data extract; if the function not work correctly, he must be exposed in errorlog 

        @return: if successful execute returns True, else returns False
        """

        output = self.generic_insert_into_table("AmostraAcaro", ("acaro_id", "amostra_id", "qtd"), (acaro_id, id_amostra, qtd))

        if output != "Success":
            function_arising = "insert_amostra_acaro," + output[2]
            self.error_insert_amostra_acaro(output, function_arising, json_name)
            return False
        
        return True

    def json_to_db_flow(self, exp_id: int, data_amt: str, json_file_name: str, acaros_id: tuple[int, int, int], quantity: tuple[int, int, int]):
        """
        Feature: performs all necessary functions to input the ai output json data in database and move the json file to correct_db_update folder if execute successful

        @param exp_id: the experiment id; it's get from json ia output
        @param data_amt: the sample date; it's get from json ia output
        @param json_file_name: the json that had data extract
        @param acaro_id: the id mites; it's pass manualy; id 1 mean spider mite, id 2 mean predeator mite and id 3 mean generalist predeator mite
        @param quantity: the qunatity of each mite; it's get from json ai output, get  
        """

        insert_amostra_success = self.insert_amostra(exp_id, data_amt, json_file_name)
        if insert_amostra_success:
            id_new_amostra = self.get_id_amostra(exp_id, data_amt, json_file_name)
            if id_new_amostra != -1:
                for i in range(len(acaros_id)):
                    insert_amostra_acaro_success = self.insert_amostra_acaro(acaros_id[i], id_new_amostra, quantity[i], json_file_name)

                    if not insert_amostra_acaro_success:
                        return 
                
                move_file(json_file_name, AI_OUTPUT_PATH, CORRECT_DB_UPDATE_PATH)

    def conection_config(self) -> dict:  # todo: connection_config must get info from .env file
        """
        Feature: access the .env file and extract important data to connect python to mysql database
        
        @return: a dictonary tha contains the important data to connect python to mysql database
        """

        load_dotenv(self.env_file)

        conect_config = {
            "host": "localhost",  # todo: os.dotenv(FILE_NAME)
            "user": "admin",
            "password": "12345",
            "database": "Inventario",
        }

        return conect_config

