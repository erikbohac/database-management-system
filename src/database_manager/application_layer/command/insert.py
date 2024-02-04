"""
Insert Command Module

This module defines the Insert command class.

Classes:
    Insert: A command class for inserting data.

"""


from .command import CommandInterface


class Insert(CommandInterface):
    """
    Insert Command Class

    A command class for inserting data.

    Methods:
        execute: Executes the insert command.

    """

    def __init__(self, application):
        """
        Initializes the Insert command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the insert command.

        Raises:
            Exception: If the action cannot be performed when not in manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            self.application.crud_operation(self.application.CRUDOperation.INSERT)
