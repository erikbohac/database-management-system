"""
Command Interface Module

This module defines the CommandInterface abstract base class.

Classes:
    CommandInterface: An abstract base class defining the structure for command objects.

"""


from abc import ABC, abstractmethod


class CommandInterface(ABC):
    """
    Command Interface Class

    An abstract base class defining the structure for command objects.

    Methods:
        execute: An abstract method to be implemented by concrete command classes.

    """
    def __init__(self, application):
        """
        Initializes the CommandInterface with the application instance.

        Args:
            application: The application instance.

        """
        self.application = application

    @abstractmethod
    def execute(self):
        """
        Abstract method to be implemented by concrete command classes.

        """
        raise NotImplementedError
