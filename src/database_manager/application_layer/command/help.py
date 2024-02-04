"""
Help Command Module

This module defines the Help command class.

Classes:
    Help: A command class for displaying help information.

"""


from .command import CommandInterface


class Help(CommandInterface):
    """
    Help Command Class

    A command class for displaying help information.

    Methods:
        execute: Executes the help command.

    """

    def __init__(self, application):
        """
        Initializes the Help command with the application instance.

        Args:
            application: The application instance.

        """

        super().__init__(application)

    def execute(self):
        """
        Executes the help command.

        Returns:
            str: A formatted menu of available commands.

        """

        menu = ('Commands:'
                '\n\tGlobal commands:'
                '\n\t\thelp \t- shows this table'
                '\n\t\texit \t- terminates the program'
                '\n\t\tconnect - try connection to database'
                '\n\t\tmanager - switch to database manager mode'
                '\n\tManager commands:'
                '\n\t\tinsert \t- inserts new row into database'
                '\n\t\tupdate \t- updates specified row'
                '\n\t\tdelete \t- deletes specified row'
                '\n\t\tselect \t- returns specified row/all rows'
                '\n\t\ttables \t- returns all available tables'
                '\n\t\timport \t- imports data into table'
                '\n\t\treport \t- generates report')

        return menu
