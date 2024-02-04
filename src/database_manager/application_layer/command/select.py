"""
Select Command Module

This module defines the Select command class.

Classes:
    Select: A command class for selecting rows from the database.

"""


from .command import CommandInterface


class Select(CommandInterface):
    """
    Select Command Class

    A command class for selecting rows from the database.

    Methods:
        execute: Executes the select command.

    """

    def __init__(self, application):
        """
        Initializes the Select command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the select command.

        Raises:
            Exception: If the action is attempted outside manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            self.application.crud_operation(self.application.CRUDOperation.SELECT)
