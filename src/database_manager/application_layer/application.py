"""
Application Module

This module defines the Application class for managing the database application.

Classes:
    Application: A class representing the database application.

"""


import xml.etree.ElementTree as Et
from enum import Enum
from .command import *
from .logics import *


class Application:
    """
    A class representing the database application.

    Attributes:
        XML_SUFFIX (str): The suffix for XML files.
        is_running (bool): Indicates whether the application is running.
        is_in_manager_mode (bool): Indicates whether the application is in manager mode.
        _data_manager: The DataManager object for managing database operations.
        _controller: The Controller object for handling user interactions.
        database_name (str): The name of the database being managed.
        xml_path (str): The path to the XML file for data import.
        _logger: The logger object for logging application events.
        invoker: The Invoker object for executing commands.

    """

    XML_SUFFIX = '.xml'

    def __init__(self, xml_import, logger):
        """
        Initializes an Application object with the provided parameters.

        Args:
            xml_import (str): The path to the XML file for data import.
            logger: The logger object for logging application events.

        """

        self.is_running = False
        self.is_in_manager_mode = False
        self._data_manager = None
        self._controller = None
        self.database_name = None
        self.xml_path = xml_import
        self._logger = logger
        self.invoker = Invoker()

    class CRUDOperation(Enum):
        """
        An enumeration representing CRUD operations.

        """

        INSERT = 'insert'
        UPDATE = 'update'
        DELETE = 'delete'
        SELECT = 'select'

    def initialize_invoker(self):
        """
        Initializes the invoker object with commands.

        """

        self.invoker.add_command('help', Help(self))
        self.invoker.add_command('exit', Exit(self))
        self.invoker.add_command('connect', Connect(self))
        self.invoker.add_command('manager', Manager(self))
        self.invoker.add_command('insert', Insert(self))
        self.invoker.add_command('tables', Tables(self))
        self.invoker.add_command('update', Update(self))
        self.invoker.add_command('select', Select(self))
        self.invoker.add_command('delete', Delete(self))
        self.invoker.add_command('import', DataImport(self))
        self.invoker.add_command('report', Report(self))

    def set_controller(self, controller):
        """
        Sets the controller object for the application.

        Args:
            controller: The controller object.

        """

        self._controller = controller

    def set_data_manager(self, data_manager):
        """
        Sets the data manager object for the application.

        Args:
            data_manager: The data manager object.

        """

        self._data_manager = data_manager

    def get_data_manager(self):
        """
        Retrieves the data manager object.

        Returns:
            DataManager: The data manager object.

        """

        return self._data_manager

    def start(self):
        """
        Starts the application in loop until user exits.

        """

        self.is_running = True
        self.database_name = self._data_manager.database_name
        while self.is_running:
            command = self._controller.get_input(subdir=[self.database_name] if self.is_in_manager_mode else None)
            try:
                output = self.invoker.execute_command(command)
                if output is not None:
                    self._controller.print_message(output)
                    self._logger.info(output)
            except Exception as e:
                self._controller.print_error(e)
                self._logger.error(e)

    def crud_operation(self, operation: CRUDOperation):
        """
        Executes a CRUD operation.

        Args:
            operation (CRUDOperation): The CRUD operation.

        """

        operation = operation.value

        table_name = self._controller.get_input(subdir=[self.database_name, 'SELECT TABLE'])
        if table_name == 'exit':
            return
        if str(table_name).lower() not in self._data_manager.get_tables():
            raise Exception(f'Table "{table_name}" does not exist')

        class_name, params = self._data_manager.get_class_attributes(table_name, operation, False)
        values = self.get_user_table_data(class_name, params)

        lines = self._data_manager.make_operation(operation, values, class_name)
        if operation == self.CRUDOperation.SELECT.value:
            self._controller.print_table(list(params.keys()), lines)
        else:
            self._controller.print_message('Operation was successfully executed')

    def get_user_table_data(self, class_name, params):
        """
        Gets user input for table data.

        Args:
            class_name (str): The name of the class.
            params (dict): The parameters of the class.

        Returns:
            list: A list of user-provided table data.

        """

        user_params = []

        for param in params:
            data_type = str(params[param]).split("'")[1].upper()
            user_data = self._controller.get_input(subdir=[self.database_name, class_name, f'{param}<{data_type}>'])
            try:
                if type(params[param]) is type(Enum):
                    user_data = user_data.upper()
                converted_input = validate_input(params[param], user_data)
                user_params.append(converted_input)
            except:
                raise Exception(f'Invalid data type, expected "{data_type}"')

        return user_params

    def xml_import(self, path):
        """
        Imports data from an XML file.

        Args:
            path (str): The path to the XML file.

        Returns:
            str: A message indicating the result of the import operation.

        """

        try:
            xml_string = load_file(path, self.XML_SUFFIX)
        except Exception as e:
            raise Exception(str(e))

        try:
            root = Et.fromstring(xml_string)
            element_name, element_data = load_xml(root)
        except Et.ParseError:
            raise Exception(f'File not in "{self.XML_SUFFIX[1:]}" format')
        except Exception as e:
            raise Exception(str(e))

        if root is None:
            raise Exception(f'File "{path}" does not contain any data')

        if element_name.lower() not in self._data_manager.get_tables():
            raise Exception('Invalid data, table to be imported in does not exist')

        class_name, params = self._data_manager.get_class_attributes(element_name, self.CRUDOperation.INSERT, False)
        retyped_data = retype_data(element_data, params)

        if self._data_manager.import_data(class_name, retyped_data, list(params.keys())):
            return f'Data successfully imported into table "{element_name}"'
        else:
            return 'Data import was unsuccessful'

    def report(self):
        """
        Generates a report from the database.

        """

        views = self._data_manager.get_views()
        self._controller.print_choice(views)

        choice = self._controller.get_input(subdir=[self.database_name, 'REPORTS'])
        if choice == 'exit':
            return

        try:
            choice = int(choice)
        except:
            raise Exception('Invalid choice selected')

        if choice <= 0 or choice > len(views):
            raise Exception(f'Choice must be between 1 and {len(views)}')

        selected_view = str(views[choice - 1]).replace(' ', '_')
        headers, report_text = self._data_manager.get_report(selected_view)

        self._controller.print_table(headers, report_text)
