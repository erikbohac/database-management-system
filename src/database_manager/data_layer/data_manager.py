"""
DataManager Module

This module defines the DataManager class for managing database operations.

Classes:
    DataManager: A class for managing database operations.

"""


from .query.builder import QueryBuilder
from .table import *


class DataManager:
    """
    A class for managing database operations.

    Attributes:
        _connection: The connection object to the database.
        _application: The application object associated with the DataManager instance.
        database_name (str): The name of the database being managed.
        query_builder (QueryBuilder): An instance of the QueryBuilder class for constructing SQL queries.
        _tables (list): A list of table names in the database.

    """

    def __init__(self, connection, database_name):
        """
        Initializes a DataManager object with the provided connection and database name.

        Args:
            connection: The connection object to the database.
            database_name (str): The name of the database being managed.

        """

        self._connection = connection
        self._application = None
        self.database_name = database_name
        self.query_builder = QueryBuilder()
        self._tables = ['owner', 'bidder', 'item', 'offer', 'winning offer', 'auction']

    def set_application(self, application):
        """
        Sets the application object associated with the DataManager instance.

        Args:
            application: The application object to be associated with the DataManager.

        """

        self._application = application

    def get_tables(self):
        """
        Retrieves a list of table names in the database.

        Returns:
            list: A list of table names.

        """

        return self._tables

    def try_connection(self):
        """
        Attempts to establish a connection to the database.

        Returns:
            bool: True if the connection is successful, False otherwise.

        """

        try:
            if self._connection.get_connection() is not None:
                return True
        except:
            return False

    def get_class_attributes(self, class_name: str, operation: str, is_import: bool):
        """
        Retrieves the attributes of a specified class for a database operation.

        Args:
            class_name (str): The name of the class.
            operation (str): The database operation ('insert', 'delete', 'select', 'update').
            is_import (bool): Indicates if the operation is an import.

        Returns:
            tuple: A tuple containing the class name and its attributes.

        """

        class_name = class_name.title().replace(' ', '')
        cls = globals().get(class_name)
        constructor = getattr(cls, '__init__')
        annotations = constructor.__annotations__.copy()
        if not is_import:
            if operation == 'insert':
                if 'identifier' in annotations:
                    annotations.pop('identifier')
        return class_name, annotations

    def make_operation(self, operation: str, user_data: list, class_name: str):
        """
        Executes a database operation based on the provided parameters.

        Args:
            operation (str): The database operation ('insert', 'delete', 'select', 'update').
            user_data (list): The data provided by the user for the operation.
            class_name (str): The name of the class associated with the operation.

        Returns:
            list: The output of the executed query.

        """

        query_selector = {
            'insert': self.query_builder.create_insert,
            'delete': self.query_builder.create_delete,
            'select': self.query_builder.create_select,
            'update': self.query_builder.create_update
        }

        class_object = globals().get(class_name)
        if operation == 'insert':
            user_data.insert(0, None)
        instance_object = class_object(*user_data,)

        query, data = query_selector[operation](instance_object)

        return self.execute_query(query, data)

    def execute_query(self, query: str, data: list):
        """
        Executes a SQL query.

        Args:
            query (str): The SQL query to execute.
            data (list): The data values to be used in the query.

        Returns:
            list: The output of the executed query.

        """

        conn = self._connection.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(query, data)
            output = cursor.fetchall()
        except Exception as e:
            raise Exception(str(e).split(':')[1].strip())

        conn.commit()
        cursor.close()

        return output

    def import_data(self, class_name: str, data: list, attributes: list):
        """
        Imports data into the database.

        Args:
            class_name (str): The name of the class associated with the data.
            data (list): The data to be imported.
            attributes (list): The attributes of the class associated with the data.

        Returns:
            bool: True if the import is successful, False otherwise.

        """

        class_object = globals().get(class_name)
        object_list = []

        for entry in data:
            new_entry = [entry[key] for key in attributes]
            object_list.append(class_object(*new_entry,))

        query, values = self.query_builder.create_import_insert(object_list)

        return self.execute_multiple_query(query, values)

    def execute_multiple_query(self, query: str, data: list):
        """
        Executes multiple SQL queries.

        Args:
            query (str): The SQL query to execute.
            data (list): The data values to be used in the queries.

        Returns:
            bool: True if the queries are executed successfully, False otherwise.

        """

        conn = self._connection.get_connection()
        cursor = conn.cursor()

        try:
            cursor.executemany(query, data)
        except Exception as e:
            raise Exception(str(e).split(':')[1].strip())

        conn.commit()
        cursor.close()

        return True

    def get_views(self):
        """
        Retrieves the views in the database.

        Returns:
            list: A list of view names.

        """

        conn = self._connection.get_connection()
        cursor = conn.cursor()

        query = f'SELECT TABLE_NAME FROM information_schema.VIEWS WHERE TABLE_SCHEMA = %s;'

        try:
            cursor.execute(query, [self.database_name])
            output = cursor.fetchall()
            output = [str(line[0]).replace('_', ' ') for line in output]
        except Exception as e:
            raise Exception(str(e).split(':')[1].strip())

        conn.commit()
        cursor.close()

        return output

    def get_report(self, report: str):
        """
        Retrieves a report from the database.

        Args:
            report (str): The name of the report to retrieve.

        Returns:
            tuple: A tuple containing the headers and data of the report.

        """

        conn = self._connection.get_connection()
        cursor = conn.cursor()

        headers = f'DESCRIBE {report};'
        query = f'SELECT * FROM {report};'

        try:
            cursor.execute(headers)
            headers_output = [column[0] for column in cursor.fetchall()]

            cursor.execute(query)
            output = cursor.fetchall()
        except Exception as e:
            raise Exception(str(e).split(':')[1].strip())

        conn.commit()
        cursor.close()

        return headers_output, output
