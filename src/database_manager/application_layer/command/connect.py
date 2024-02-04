"""
Connect Command Module

This module defines the Connect command class.

Classes:
    Connect: A command class for connecting to the database.

"""


from .command import CommandInterface


class Connect(CommandInterface):
    """
    Connect Command Class

    A command class for connecting to the database.

    Methods:
        execute: Executes the connect command.

    """

    def __init__(self, application):
        """
        Initializes the Connect command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the connect command.

        Returns:
            str: A message indicating successful connection.

        Raises:
            Exception: If there was a problem connecting to the database.

        """

        if self.application.get_data_manager().try_connection():
            return 'Successfully connected to database'
        else:
            raise Exception('There was a problem connecting to database')
