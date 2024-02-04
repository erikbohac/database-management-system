"""
Bidder Module

This module defines the Bidder class for managing bidder entities.

Classes:
    Bidder: A class representing a bidder entity.

"""


from .database_entity import DatabaseEntity


class Bidder(DatabaseEntity):
    """
    A class representing a bidder entity.

    Attributes:
        identifier (int): The unique identifier of the bidder.
        surname (str): The surname of the bidder.
        last_name (str): The last name of the bidder.
        address (str): The address of the bidder.
        post_code (int): The postal code of the bidder.
        phone_number (str): The phone number of the bidder.

    """

    def __init__(self, identifier: int, surname: str, last_name: str, address: str, post_code: int, phone_number: str):
        """
        Initializes a Bidder object with the provided attributes.

        Args:
            identifier (int): The unique identifier of the bidder.
            surname (str): The surname of the bidder.
            last_name (str): The last name of the bidder.
            address (str): The address of the bidder.
            post_code (int): The postal code of the bidder.
            phone_number (str): The phone number of the bidder.

        """

        super().__init__(identifier)
        self.surname = surname
        self.last_name = last_name
        self.address = address
        self.post_code = post_code
        self.phone_number = phone_number
