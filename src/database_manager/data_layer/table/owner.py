"""
Owner Module

This module defines the Owner class for managing owner entities.

Classes:
    Owner: A class representing an owner entity.

"""


from .database_entity import DatabaseEntity


class Owner(DatabaseEntity):
    """
    A class representing an owner entity.

    Attributes:
        identifier (int): The unique identifier of the owner.
        surname (str): The surname of the owner.
        last_name (str): The last name of the owner.
        address (str): The address of the owner.
        post_code (int): The postal code of the owner.
        phone_number (str): The phone number of the owner.
        is_verified (bool): Indicates whether the owner is verified.
        email (str): The email address of the owner.

    """

    def __init__(self, identifier: int, surname: str, last_name: str, address: str, post_code: int, phone_number: str, is_verified: bool, email: str):
        """
        Initializes an Owner object with the provided attributes.

        Args:
            identifier (int): The unique identifier of the owner.
            surname (str): The surname of the owner.
            last_name (str): The last name of the owner.
            address (str): The address of the owner.
            post_code (int): The postal code of the owner.
            phone_number (str): The phone number of the owner.
            is_verified (bool): Indicates whether the owner is verified.
            email (str): The email address of the owner.

        """

        super().__init__(identifier)
        self.surname = surname
        self.last_name = last_name
        self.address = address
        self.post_code = post_code
        self.phone_number = phone_number
        self.is_verified = is_verified
        self.email = email
