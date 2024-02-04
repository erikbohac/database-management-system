"""
Manager Command Module

This module defines the Manager command class.

Classes:
    Manager: A command class for activating manager mode.

"""

from .command import CommandInterface


class Manager(CommandInterface):
    """
    Manager Command Class

    A command class for activating manager mode.

    Methods:
        execute: Executes the manager command.

    """

    def __init__(self, application):
        """
        Initializes the Manager command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the manager command.

        Returns:
            str: Message indicating the status of manager mode activation.

        Raises:
            Exception: If there is a problem connecting to the database.

        """

        if self.application.is_in_manager_mode:
            return 'Manager mode already activated'
        if self.application.get_data_manager().try_connection():
            self.application.is_in_manager_mode = True
            return 'Manager mode activated'
        else:
            raise Exception('There was a problem connecting to the database')
