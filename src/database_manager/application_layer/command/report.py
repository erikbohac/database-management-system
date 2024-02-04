"""
Report Command Module

This module defines the Report command class.

Classes:
    Report: A command class for generating reports.

"""


from .command import CommandInterface


class Report(CommandInterface):
    """
    Report Command Class

    A command class for generating reports.

    Methods:
        execute: Executes the report command.

    """

    def __init__(self, application):
        """
        Initializes the Report command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the report command.

        Returns:
            str: Message indicating the result of generating the report.

        Raises:
            Exception: If the action is attempted outside manager mode.

        """

        if not self.application.is_in_manager_mode:
            raise Exception('To perform this action, you must be in manager mode')
        else:
            return self.application.report()
