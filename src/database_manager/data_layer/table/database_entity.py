"""
Database Entity Module

This module defines the DatabaseEntity class, which serves as the base class for database entities.

Classes:
    DatabaseEntity: An abstract base class representing a database entity.

"""


from abc import ABC


class DatabaseEntity(ABC):
    """
    An abstract base class representing a database entity.

    Attributes:
        id (int): The unique identifier of the database entity.

    """

    def __init__(self, identifier: int):
        """
        Initializes a DatabaseEntity object with the provided identifier.

        Args:
            identifier (int): The unique identifier of the database entity.

        """

        self.id = identifier
    