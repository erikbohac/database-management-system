"""
WinningOffer Module

This module defines the WinningOffer class for managing winning offer entities.

Classes:
    WinningOffer: A class representing a winning offer entity.

"""


from .database_entity import DatabaseEntity


class WinningOffer(DatabaseEntity):
    """
    A class representing a winning offer entity.

    Attributes:
        identifier (int): The unique identifier of the winning offer.
        offer_id (int): The unique identifier of the offer that won the auction.

    """

    def __init__(self, identifier: int, offer_id: int):
        """
        Initializes a WinningOffer object with the provided attributes.

        Args:
            identifier (int): The unique identifier of the winning offer.
            offer_id (int): The unique identifier of the offer that won the auction.

        """

        super().__init__(identifier)
        self.offer_id = offer_id
