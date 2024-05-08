from dotenv import load_dotenv
from types import NoneType
import mysql.connector
from __init__ import SAMPLE_ID_SQL_FILE, INSERT_SAMPLE_SQL_FILE, INSERT_FOLIOLO_SQL_FILE
import os

def read_file(path: str) -> str | NoneType:
    """
    Feature: Function responsible for reading files

    @param path: File to read
    
    @return: None
    """
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


class MySQL_Response:
    """Class responsible for establishing the responses that the functions will return"""
    def __init__(self, *, confirmation: bool, data: list | NoneType = None, error: int | NoneType = None, msg_error: str | NoneType = None):
        self.confirmation = confirmation
        self.data = data
        self.error = None
        self.msg_error = None
        if not self.confirmation:
            self.error = error
            self.msg_error = msg_error


class MySQL_Connection:
    """Class responsible for establishing connection to the Database"""
    # SELECT FILES
    SQLFILE_SELECT_SAMPLEID = SAMPLE_ID_SQL_FILE

    # INSERT FILES
    SQLFILE_INSERT_SAMPLE = INSERT_SAMPLE_SQL_FILE
    SQLFILE_INSERT_FOLIOLO = INSERT_FOLIOLO_SQL_FILE


    def __init__(self, env_file: str):
        self.env_file = env_file
    

    def insert_sample(self, data_Amos: str, cultivo_id: int, classificacao_final: str, media_rajado_foliolo: float, acao_sugerida: str, qtd_total: int, seis_a_nove: float, mais_dez: float, um_a_cinco: float, sem_predador_rajado: float, predador_sem_rajado: float, com_predador_rajado: float) -> MySQL_Response:
        """
        Feature: Function responsible for performing INSERT in the SAMPLE table with a given Planting ID and Timestamp.
        
        @params:
            - cultivo_id: int,
            - data_Amos: str,
            - classificacao_final, 
            - media_rajado_foliolo, 
            - acao_sugerida, 
            - qtd_total, 
            - seis_a_nove, 
            - mais_dez, 
            - um_a_cinco, 
            - sem_predador_rajado, 
            - predador_sem_rajado, 
            - com_predador_rajado

        @return:
            MySQL_Response:
                Attributes:
                - confirmation: bool -> Whether the operation was successful or not;
                - data: NoneType -> Not used in this function;
                - error: int (when applicable) | NoneType -> error code, if any;
                    - error = 0 -> SQL file not found;
                    - error = 1 -> Connection not established;
                    - error = 2 -> error executing SQL;
                - msg_error: str (when applicable) | NoneType -> Description of the error, if any;
        """
        
        sql_code = read_file(self.SQLFILE_INSERT_SAMPLE)
        if sql_code is None:
            return MySQL_Response(confirmation = False, error = 0)
        
        load_dotenv(self.env_file)
        connection_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
            "port": os.getenv("MYSQL_PORT")
        }

        try:
            connection = mysql.connector.connect(**connection_config) 
            cursor = connection.cursor()
        except Exception as e:
            return MySQL_Response(confirmation = False, error = 1)

        try:
            params = (data_Amos, cultivo_id, classificacao_final, media_rajado_foliolo, acao_sugerida, qtd_total, seis_a_nove, mais_dez, um_a_cinco, sem_predador_rajado, predador_sem_rajado, com_predador_rajado)

            cursor.execute(sql_code, params = params)
            connection.commit()
        except Exception as e:
            connection.close()
            return MySQL_Response(confirmation = False, error = 2, msg_error = e)
        
        cursor.close()
        connection.close() 

        return MySQL_Response(confirmation = True)
        

    def select_sample_id(self, data_Amos: str, cultivo_id: int) -> MySQL_Response:
        """
        Feature: Function responsible for performing SELECT on the SAMPLE table in search of the ID with a given Cultivation ID and Timestamp.

        @params:
            - cultivo_id: int;
            - data_Amos: str.

        @return:
            confirmation[bool], error[int], msg_error[str], id[int]

            - confirmation: True if the SELECT is successful, False otherwise;
            - error: Signaling flag
                - -1: Executed correctly;
                - 0: SQL file not found;
                - 1: Connection not established;
                - 2: Error executing SQL;
                - 3: Indicates that an error occurred while executing the SQL query;
            - msg_error: Used only if confirmation == False and error = 2. Returns the description of the MySQL error.
            - output: Sample Id 
        """ 
        
        sql_code = read_file(self.SQLFILE_SELECT_SAMPLEID)
        if sql_code is None:
            return MySQL_Response(confirmation = False, error = 0)
        
        load_dotenv(self.env_file)
        connection_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
            "port": os.getenv("MYSQL_PORT")
        }

        try:
            connection = mysql.connector.connect(**connection_config) 
            cursor = connection.cursor()
        except:
            return MySQL_Response(confirmation = False, error = 1)

        try:
            params = (data_Amos, cultivo_id)
            cursor.execute(sql_code, params = params)

            output = cursor.fetchall()
            if len(output) > 0:
                output = output[0][0]
            else:
                return MySQL_Response(confirmation = False, error = 3)
        except Exception as e:
            connection.close()
            return MySQL_Response(confirmation = False, error = 2, msg_error = e)
        
        cursor.close()
        connection.close() 

        return MySQL_Response(confirmation = True, data = output)


    def insert_leafs(self, imgOrig:str, imgProc:str, qntRaj: int, qntMacro: int, qntCali: int, sample_id: int) -> MySQL_Response:
        """
        Feature: Function responsible for performing INSERT in the QUANTIDADE_FRUTO table with a given Sample ID, Category ID and Quantity.

        @params: 
            - sample_id: int; 
            - categories_id: int;
            - quantity: int or str.
        
        @return:
            MySQL_Response:
                Attributes:
                - confirmation: bool -> Whether the operation was successful or not;
                - data: NoneType -> Not used in this function;
                - error: int (when applicable) | NoneType -> error code, if any;
                    - error = 0 -> SQL file not found;
                    - error = 1 -> Connection not established;
                    - error = 2 -> error executing SQL;
                - msg_error: str (when applicable) | NoneType -> Description of the error, if any;
        """
        
        sql_code = read_file(self.SQLFILE_INSERT_FOLIOLO)
        if sql_code is None:
            return MySQL_Response(confirmation = False, error = 0)
        
        load_dotenv(self.env_file)
        connection_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
            "port": os.getenv("MYSQL_PORT")
        }

        try:
            connection = mysql.connector.connect(**connection_config) 
            cursor = connection.cursor()
        except:
            return MySQL_Response(confirmation = False, error = 1)

        try:
            params = (imgOrig, imgProc, qntRaj, qntMacro, qntCali, sample_id)

            cursor.execute(sql_code, params = params)
            connection.commit()
        except Exception as e:
            connection.close()
            return MySQL_Response(confirmation = False, error = 2, msg_error = e)
        
        cursor.close()
        connection.close() 

        return MySQL_Response(confirmation = True)
        