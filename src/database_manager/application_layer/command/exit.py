"""
Exit Command Module

This module defines the Exit command class.

Classes:
    Exit: A command class for exiting the program.

"""


from .command import CommandInterface


class Exit(CommandInterface):
    """
    Exit Command Class

    A command class for exiting the program.

    Methods:
        execute: Executes the exit command.

    """

    def __init__(self, application):
        """
        Initializes the Exit command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the exit command.

        Returns:
            str: A message indicating termination of the program.

        """

        if self.application.is_in_manager_mode:
            self.application.is_in_manager_mode = False
        else:
            self.application.is_running = False
            message = 'Program terminated..'
            return message
