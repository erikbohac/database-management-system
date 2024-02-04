"""
Tables Command Module

This module defines the Tables command class.

Classes:
    Tables: A command class for retrieving available tables.

"""


from .command import CommandInterface


class Tables(CommandInterface):
    """
    Tables Command Class

    A command class for retrieving available tables.

    Methods:
        execute: Executes the tables command.

    """

    def __init__(self, application):
        """
        Initializes the Tables command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the tables command.

        Returns:
            str: Message listing the available tables.

        Raises:
            Exception: If the action is attempted outside manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            tables = self.application.get_data_manager().get_tables()
            output = 'Available tables:'
            for value in tables:
                output += f'\n\t - {value.capitalize()}'
            return output
