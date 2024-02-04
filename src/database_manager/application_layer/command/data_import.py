"""
Data Import Command Module

This module defines the DataImport command class.

Classes:
    DataImport: A command class for importing data.

"""


from .command import CommandInterface


class DataImport(CommandInterface):
    """
    Data Import Command Class

    A command class for importing data.

    Methods:
        execute: Executes the data import command.

    """

    def __init__(self, application):
        """
        Initializes the DataImport command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the data import command.

        Returns:
            str: A message indicating success or failure of the data import.

        Raises:
            Exception: If the action cannot be performed when not in manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            return self.application.xml_import(self.application.xml_path)
