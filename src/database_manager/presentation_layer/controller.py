"""
Controller

This module provides a class for handling user interactions and printing formatted messages.

Classes:
    Controller: A class for handling user interactions and printing formatted messages.

"""


from .view import *


class Controller:
    """
    A class for handling user interactions and printing formatted messages.

    Methods:
        get_input(subdir=None): Prompts the user for input and returns the entered command.
        print_outlined_message(message: str, length: int): Prints a message surrounded by a border.
        print_table(headers: list, values: list): Prints a table with headers and corresponding values.
        print_message(message: str): Prints a message.
        print_error(message: str): Prints an error message.
        print_choice(options: str): Prints a list of options for user choice.

    """

    def __init__(self):
        """
        Initializes the Controller instance.
        """

        pass

    def get_input(self, subdir=None):
        """
        Prompts the user for input and returns the entered command.

        Args:
            subdir (str, optional): A subdirectory string to be displayed in the console prompt.

        Returns:
            str: The user-entered command.

        """

        text = 'Console:~$ '
        if subdir is not None:
            text = reformat_console_text(text, subdir)
        text = replace_chars(text)
        command = input(text).strip()
        return command

    def print_outlined_message(self, message: str, length: int):
        """
        Prints a message surrounded by a border.

        Args:
            message (str): The message to be printed.
            length (int): The length of the border.

        """

        output = outline_text(message, length)
        print(output)

    def print_table(self, headers: list, values: list):
        """
        Prints a table with headers and corresponding values.

        Args:
            headers (list): A list of strings representing table headers.
            values (list): A list of lists representing table values.

        """

        table, length = generate_text_table(headers, values)
        self.print_outlined_message(table, length)

    def print_message(self, message: str):
        """
        Prints a message.

        Args:
            message (str): The message to be printed.

        """

        print(message)

    def print_error(self, message: str):
        """
        Prints an error message.

        Args:
            message (str): The error message to be printed.

        """

        print(f'Error: {message}')

    def print_choice(self, options: str):
        """
        Prints a list of options for user choice.

        Args:
            options (str): A string containing the options to be printed.

        """

        option_string = 'Options:'
        for index in range(len(options)):
            option_string += f'\n\t{index + 1}. {options[index]}'
        print(option_string)
