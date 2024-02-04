"""
Invoker Module

This module defines the Invoker class responsible for executing commands.

Classes:
    Invoker: A class to execute commands.

"""


class Invoker:
    """
    Invoker Class

    A class to execute commands.

    Methods:
        add_command: Adds a command to the invoker.
        execute_command: Executes a command.

    """

    def __init__(self):
        """
        Initializes the Invoker with an empty dictionary of commands.

        """

        self._commands = {}

    def add_command(self, name, command):
        """
        Adds a command to the invoker.

        Args:
            name (str): The name of the command.
            command (CommandInterface): The command object.

        """

        self._commands[name] = command

    def execute_command(self, name):
        """
        Executes a command.

        Args:
            name (str): The name of the command to execute.

        Returns:
            str: The result of executing the command.

        Raises:
            Exception: If the command is not found.

        """

        if name == '':
            return None
        if name in self._commands.keys():
            return self._commands[name].execute()
        else:
            raise Exception('Invalid command, type "help" for more info')
