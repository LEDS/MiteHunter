from python_modules.archive_mennager import *
from python_modules.error_notification_email_confidential import try_send_email

import linecache
import sys
from datetime import datetime


ERROR_LOG_TEMPLATE = """File: {};
Line: {};
Command: {};
Type: {};
Object: {};
Changes Made: {};
Error Date: {};"""  # This is a template to error log text


class ErrorHandling:
    """
    Feature: performs error handling on expected common errors
    """
    def __init__(self):
        self.index_error = int()
        self._exception_output = tuple()
        self._json_name = str()
        self._error_log_text = str()
        self._possible_changes = tuple()
        self._generic_error = str()
        self._sent_mail = True

    def generic_error_handling(self):
        """
        Feature: performs error handling that is capable to be customized; it is important to improve code readability and reduce the number of redundant lines
        """

        self.update_error_index()
        change, text_format = self.get_correct_change_and_text_format()
        self.error_log_generator(self.possible_changes[change].format(*text_format))
        if self.sent_mail:
            try_send_email(self.error_log_text)

    def error_insert_amostra(self):
        """
        Feature: performs error handling for MySQLConnection.insert_amostra
        """

        self.possible_changes = (
                            "Nothing have change{}",
                            "The file {} should be moved to error folder, but an error ocurred\n{}",
                            "The file {} had ben moved to error folder"
        )

        self.generic_error_handling()

    def error_get_id_amostra(self):
        """
        Feature: performs error handling for MySQLConnection.get_id_amostra function
        """

        self.possible_changes = (
            "Values successful insert into table Amostra{}",
            "Values successful insert into table Amostra and the file {} should be moved to error folder, but an error ocurred\n{}",
            "Values successful insert into table Amostra and the file {} had ben moved to error folder"
        )

        self.generic_error_handling()

    def error_insert_amostra_acaro(self):
        """
        Feature: performs error handling for MySQLConnection.insert_amostra_acaro
        """

        self.possible_changes = (
            "Values had been insert into table Amostra successful",
            "Values successful insert into table Amostra and the file {} should be moved to error folder, but an error ocurred\n{}",
            "Values successful insert into table Amostra and the file {} had ben moved to error folder"
        )

        self.generic_error_handling()

    def update_error_index(self):
        """
        Feature: updates the index_error property to organize error logs and json files correctly
        """

        self.index_error = self.error_index()

    def move_file_to_error_folder(self) -> None | Exception:
        """
        Feature: move a json file to error folder

        @return: None if performer correctly | the exception code when move file fails
        """

        try:
            move_file(self._json_name, AI_OUTPUT_PATH, ERROR_DIR_PATH, f"{self.index_error}-")
        except Exception as e:
            return e
        return None

    def error_log_generator(self, changes: str):
        """
        Feature: Generates an error log in a specific folder

        @param changes: all changes mades during excecution
        """

        today = datetime.today()
        error_date = f"{today.day}-{today.month}-{today.year}"

        file_name = f"{self.index_error}-errorLog"

        self.error_log_text = ERROR_LOG_TEMPLATE.format(*self._exception_output, changes, error_date)

        with open(f"{ERROR_DIR_PATH}/{file_name}.txt", "w") as file:
            file.write(self.error_log_text)

    def get_execption_output(self):
        """
        feature: get information from error, like the error code that terminal returns when a python file is executed
        """

        exc_type, exc_obj, tb = sys.exc_info()

        f = tb.tb_frame
        line_number = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, line_number, f.f_globals)
        command_error = line.strip()

        self._exception_output = (filename, line_number, command_error, exc_type, exc_obj)

    def get_correct_change_and_text_format(self) -> tuple[int, list]:
        """
        Feature: prepares an output that indicates what changes were made (data inserted into the database, files moved, etc)

        @output: the first value of the tuple is the key to the possible change made; the second is text that will be written in case this change occurs
        """

        text_format = [""]
        change = 0

        if self.generic_error == "Error executing SQL":
            move_success = self.move_file_to_error_folder()
            text_format[0] = self.json_name

            if move_success:
                change = 1
                text_format.append(move_success)
            else:
                change = 2

        return change, text_format

    @property
    def exception_output(self) -> tuple:
        return self._exception_output

    @exception_output.setter
    def exception_output(self, value: tuple):
        self._exception_output = value

    @property
    def json_name(self) -> str:
        return self._json_name

    @json_name.setter
    def json_name(self, value: str):
        self._json_name = value

    @property
    def error_log_text(self) -> str:
        return self._error_log_text

    @error_log_text.setter
    def error_log_text(self, value: str):
        self._error_log_text = value

    @property
    def possible_changes(self) -> tuple:
        return self._possible_changes

    @possible_changes.setter
    def possible_changes(self, value: tuple):
        self._possible_changes = value

    @property
    def generic_error(self) -> str:
        return self._generic_error

    @generic_error.setter
    def generic_error(self, value: str):
        self._generic_error = value

    @property
    def sent_mail(self) -> bool:
        return self._sent_mail

    @sent_mail.setter
    def sent_mail(self, value: bool):
        self._sent_mail = value

    @staticmethod
    def error_index() -> int:
        """
        Feature: get all error logs in error directory to return the next error index

        @return: next error index
        """

        try:
            last_error_log = listdir(ERROR_DIR_PATH)[-1]
            index_error_separator = last_error_log.index("-")
            last_index = last_error_log[:index_error_separator]
        except Exception:
            last_index = 0

        return int(last_index) + 1
