"""
Update Command Module

This module defines the Update command class.

Classes:
    Update: A command class for updating specified rows in the database.

"""


from .command import CommandInterface


class Update(CommandInterface):
    """
    Update Command Class

    A command class for updating specified rows in the database.

    Methods:
        execute: Executes the update command.

    """

    def __init__(self, application):
        """
        Initializes the Update command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the update command.

        Returns:
            None

        Raises:
            Exception: If the action is attempted outside manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            self.application.crud_operation(self.application.CRUDOperation.UPDATE)
