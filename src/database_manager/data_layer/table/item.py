"""
Item Module

This module defines the Item class for managing item entities.

Classes:
    Item: A class representing an item entity.

"""


from .database_entity import DatabaseEntity


class Item(DatabaseEntity):
    """
    A class representing an item entity.

    Attributes:
        identifier (int): The unique identifier of the item.
        item_name (str): The name of the item.
        item_description (str): The description of the item.
        start_price (float): The starting price of the item.
        owner_id (int): The unique identifier of the owner of the item.

    """

    def __init__(self, identifier: int, item_name: str, item_description: str, start_price: float, owner_id: int):
        """
        Initializes an Item object with the provided attributes.

        Args:
            identifier (int): The unique identifier of the item.
            item_name (str): The name of the item.
            item_description (str): The description of the item.
            start_price (float): The starting price of the item.
            owner_id (int): The unique identifier of the owner of the item.

        """

        super().__init__(identifier)
        self.item_name = item_name
        self.item_description = item_description
        self.start_price = start_price
        self.owner_id = owner_id
