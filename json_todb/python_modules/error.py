# Feature:
# This module is responsible for storing error handling features to be used in MySQLConnection class from mysql_connection.py

# Own modules
from json_todb.python_modules.archive_mennager import *

# External modules
import linecache
import sys


def get_execption_output() -> str:  # todo: use this function more intelligently
    """
    feature: get information from error, like the error code that terminal returns when a python file is executed

    @return: a string that contains error information to be used in error log
    """
    
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}")'.format(filename, lineno, line.strip())


class ErrorHandling:
    def __init__(self):
        self.index_error = error_index()

    def generic_error_handling(self, error_code: tuple[str, Exception, str], error_function: str, file_name: str, possible_change: tuple[str, str, str]):
        """
        Feature: performs error handling that is capable to be customized; it is important to improve code readability and reduce the number of redundant lines

        @param error_code: error code that MySQLConnection class return when an error ocurred
        @param error_function: the function that return this error
        @param file_name: the json that data had ben extract 
        @param possible_change: strings that contains all possible changes mande in internal folders and database 
        """

        self.update_error_index()
        
        generical_error = error_code[0]

        if generical_error == "Connection not established":
            change = possible_change[0]
        elif generical_error == "Error executing SQL":
            move_success = self.move_file_to_error_folder(file_name)
            if move_success != True:
                change = possible_change[1].format(file_name, move_success)
            else:
                change = possible_change[2].format(file_name)
        else:
            raise "The output from generic_insert_into_table is wrong"

        formatted_error_code = ("{}, " * len(error_code)).format(*error_code)[:-2]
        function_error = "insert_amostra, " + error_function

        error_log_generator(formatted_error_code, function_error, change, self.index_error)
        
    def error_insert_amostra(self, error_code: tuple[str, Exception, str], error_function: str, file_name: str):
        """
        Feature: performs error handling for MySQLConnection.insert_amostra

        @param error_code: error code that MySQLConnection.insert_amostra function return when an error ocurred
        @param error_function: the function that return this error
        @param file_name: the json that data had ben extract 
        """

        possible_changes = (
                            "Nothing have change",
                            "The file {} should be moved to error folder, but an error ocurred\n{}",
                            "The file {} had ben moved to error folder"
        )

        self.generic_error_handling(error_code, error_function, file_name, possible_changes)
    
    def error_get_id_amostra(self, error_code: tuple[str, Exception, str], error_function: str, file_name: str):
        """
        Feature: performs error handling for MySQLConnection.get_id_amostra function

        @param error_code: error code that MySQLConnection.get_id_amostra function return when an error ocurred
        @param error_function: the function that return this error
        @param file_name: the json that data had ben extract 
        """
            
        possible_changes = (
            "Values successful insert into table Amostra",
            "Values successful insert into table Amostra and the file {} should be moved to error folder, but an error ocurred\n{}",
            "Values successful insert into table Amostra and the file {} had ben moved to error folder"
        )

        self.generic_error_handling(error_code, error_function, file_name, possible_changes)
    
    def error_insert_amostra_acaro(self, error_code: tuple[str, Exception, str], error_function: str, file_name: str):
        """
        Feature: performs error handling for MySQLConnection.insert_amostra_acaro

        @param error_code: error code that MySQLConnection.insert_amostra_acaro function return when an error ocurred
        @param error_function: the function that return this error
        @param file_name: the json that data had ben extract
        """
                
        possible_changes = (
            "Values had been insert into table Amostra successful",
            "Values successful insert into table Amostra and the file {} should be moved to error folder, but an error ocurred\n{}",
            "Values successful insert into table Amostra and the file {} had ben moved to error folder"
        )

        self.generic_error_handling(error_code, error_function, file_name, possible_changes)

    def update_error_index(self):
        """
        Feature: updates the index_error property to organize error logs and json files correctly 
        """

        self.index_error = error_index()

    def move_file_to_error_folder(self, archive_name: str) -> bool | Exception:
        """
        Feature: move a json file to error folder

        @param archive_name: the json file name that should be moved

        @return: True if performer correctly | the exception code when move file fails 
        """

        try:
            new_file_name = f"{self.index_error}-{archive_name}"
            move_file(new_file_name, AI_OUTPUT_PATH, ERROR_DIR_PATH)
        except Exception as e:
            return e
        return True

