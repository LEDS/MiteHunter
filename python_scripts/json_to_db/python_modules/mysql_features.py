from python_modules.error import ErrorHandling
from python_modules.archive_mennager import read_file, ENV_FILE_PATH

import mysql.connector
import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod


class MySQLConnection(ABC):
    """
    Feature: make the connection to mysql database
    """

    def __init__(self, env_file_path: str = ENV_FILE_PATH):
        self.env_file = read_file(env_file_path)
        self._cursor = None
        self._connection = None

    def try_make_db_connectio(self) -> bool:
        """
        Feature: try make the DB connection

        @return: True if connect correctly; False if somethin get wrong
        """

        try:
            self.make_db_connection()
            return True
        except Exception:
            self.get_execption_output()
            self.generic_error = "Connection not established"
            return False

    def conection_config(self) -> dict:
        """
        Feature: access the .env file and extract important data to connect python to mysql database
        
        @return: a dictonary tha contains the important data to connect python to mysql database
        """

        load_dotenv(self.env_file)

        conect_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_ROOT_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE")
        }

        return conect_config

    def make_db_connection(self):
        """
        Feature: do the DB connection
        """
        self.connection = mysql.connector.connect(**self.conection_config())
        self.cursor = self.connection.cursor(buffered=True)

    def finish_db_connection(self):
        """
        Feature: close the connection to DB and commit the data insert
        """

        self.connection.commit()  # Evectevily trasnfere the data insert to MySQL DB
        self.cursor.close()  # Finish the cursor
        self.connection.close()  # Finish Connection

    @abstractmethod
    def get_execption_output(self):
        pass

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = value

    @property
    @abstractmethod
    def exception_output(self):
        pass

    @exception_output.setter
    @abstractmethod
    def exception_output(self, value):
        pass

    @property
    @abstractmethod
    def generic_error(self):
        pass

    @generic_error.setter
    @abstractmethod
    def generic_error(self, value):
        pass


class MySQLCommands(ErrorHandling, MySQLConnection, ABC):
    """
    Feature: this class have usefull commands in MySQL; is used as backbone to specific commands classes
    """

    def __init__(self):
        ErrorHandling.__init__(self)
        MySQLConnection.__init__(self)

    def generate_insert_sql_code(self, values_lenght: int) -> str:
        """
        Feature: generate the mysql insert code based in how much values you want insert

        @param values_lenght: the lenght of values you want to inssert 

        @return: mysql insert code
        """

        param_names_handling = str(self.columns_insert).replace("'", "")
        values_assist = "%s," * values_lenght
        sql_code = f"INSERT INTO {self.table_name} {param_names_handling} VALUES ({values_assist[:-1]})"

        return sql_code

    def make_insert(self, values: tuple):
        """
        Feature: execute the mysql insert code

        @param values:  the values that you want to insert
        """

        sql_code = self.generate_insert_sql_code(len(values))
        self.cursor.execute(sql_code, values)

    def try_make_insert(self, values: tuple) -> bool:
        """
        Feature: try excecute the mysql insert command

        @param values:  the values that you want to insert

        @return: True if correct; False if an error occured
        """

        try:
            self.make_insert(values)
            return True
        except Exception:
            self.get_execption_output()
            self.generic_error = "Error executing SQL"
            return False

    def generate_select_sql_code(self) -> str:
        """
        Feature: generate the mysql select code

        @return: mysql select code
        """

        column_want = ("{}" * len(self.columns_want)).format(*self.columns_want)
        sql_code = f"SELECT {column_want} FROM {self.table_name}"

        if self.where:
            filter_text = ("{} = %s AND " * len(self.columns_filter)).format(*self.columns_filter)[:-5]
            sql_code += f" WHERE {filter_text}"

        return sql_code

    def do_select(self):
        """
        Feature: execute the MySQL SELECT command 
        """

        sql_code = self.generate_select_sql_code()
        if self.where:
            self.cursor.execute(sql_code, self.filter_values)
        else:
            self.cursor.execute(sql_code)

    def try_do_select(self) -> bool:
        """
        Feature: try excecute the MySQL SELECT command

        @return: True if correct; False if an error occured
        """
                
        try:
            self.do_select()
            return True
        except Exception:
            self.get_execption_output()
            self.generic_error = "Error executing SQL"
            return False

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    @table_name.setter
    @abstractmethod
    def table_name(self, value: str):
        pass

    @property
    @abstractmethod
    def columns_insert(self) -> tuple:
        pass

    @columns_insert.setter
    @abstractmethod
    def columns_insert(self, value: tuple):
        pass

    @property
    @abstractmethod
    def where(self):
        pass

    @property
    @abstractmethod
    def columns_filter(self) -> tuple:
        pass

    @property
    @abstractmethod
    def columns_want(self) -> list:
        pass

    @property
    @abstractmethod
    def filter_values(self) -> tuple:
        pass


class MySQLJsonToDB(MySQLCommands):
    """
    Feature: create a specific class to insert AI outputs into the DB
    """

    def __init__(self):
        MySQLCommands.__init__(self)

        self._table_name = str()
        self._columns_insert = tuple()
        self._sample_data = tuple()  # todo: verificar a saída do json
        self._mites_quantity = tuple()
        self._mites_id = (1, 2, 3)  # 1 = spider mite; 2 = predator mite; 3 = generalist predeator mite
        self._where = True
        self._columns_want = ["id"]
        self._columns_filter = ("data_amostra", "experimento_id")

    def insert_amostra(self) -> bool:  # data_amostra should be like "year-month-day"
        """
        Feature: insert past values into the Amostra table and handle possible errors

        @return: if successful execute returns True, else returns False
        """

        self.table_name = "Amostra"
        self.columns_insert = ("data_amostra", "experimento_id")
        return self.try_make_insert(self.sample_data)

    def get_id_amostra(self) -> int:
        """
        Feature: get id from Amostra table and handle possible errors

        @return: if successful execute returns True, else returns False
        """

        self.table_name = "Amostra"

        if not self.try_do_select():
            return -1

        amostra_id = self.cursor.fetchone()
        amostra_id = amostra_id[0] if len(amostra_id) > 0 else -1

        if amostra_id == -1:
            self.error_get_id_amostra()

        return amostra_id

    def insert_amostra_acaro(self) -> bool:
        """
        Feature: insert past values into the AmostraAcaro table and handle possible errors

        @return: if successful execute returns True, else returns False
        """

        self.columns_insert = ("acaro_id", "amostra_id", "qtd")

        sample_id = self.get_id_amostra()

        self.table_name = "AmostraAcaro"
        quantity_iterator = 0

        if sample_id == -1:
            return False

        for mite in self._mites_id:
            values_to_insert = (mite, sample_id, self.mites_quantity[quantity_iterator])
            quantity_iterator += 1

            if not self.try_make_insert(values_to_insert):
                self.connection.rollback()
                return False
        return True

    @property
    def table_name(self) -> str:
        return self._table_name

    @table_name.setter
    def table_name(self, value: str):
        self._table_name = value

    @property
    def columns_insert(self) -> tuple:
        return self._columns_insert

    @columns_insert.setter
    def columns_insert(self, value: tuple):
        self._columns_insert = value

    @property
    def sample_data(self) -> tuple:
        return self._sample_data

    @sample_data.setter
    def sample_data(self, value: tuple):
        self._sample_data = value

    @property
    def mites_quantity(self) -> tuple[int, int, int]:
        return self._mites_quantity

    @mites_quantity.setter
    def mites_quantity(self, value: tuple[int, int, int]):
        self._mites_quantity = value

    @property
    def where(self) -> bool:
        return self._where

    @property
    def columns_filter(self) -> tuple:
        return self._columns_filter

    @property
    def columns_want(self) -> list:
        return self._columns_want

    @property
    def filter_values(self) -> tuple:
        return self._sample_data
