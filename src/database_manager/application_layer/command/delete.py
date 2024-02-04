"""
Delete Command Module

This module defines the Delete command class.

Classes:
    Delete: A command class for deleting data.

"""


from .command import CommandInterface


class Delete(CommandInterface):
    """
    Delete Command Class

    A command class for deleting data.

    Methods:
        execute: Executes the delete command.

    """

    def __init__(self, application):
        """
        Initializes the Delete command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the delete command.

        Raises:
            Exception: If the action cannot be performed when not in manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            self.application.crud_operation(self.application.CRUDOperation.DELETE)
