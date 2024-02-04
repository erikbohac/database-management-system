"""
Offer Module

This module defines the Offer class for managing offer entities.

Classes:
    Offer: A class representing an offer entity.

"""


from datetime import datetime
from .database_entity import DatabaseEntity


class Offer(DatabaseEntity):
    """
    A class representing an offer entity.

    Attributes:
        identifier (int): The unique identifier of the offer.
        amount (float): The amount of the offer.
        offer_date (datetime): The date and time when the offer was made.
        auction_id (int): The unique identifier of the auction associated with the offer.
        bidder_id (int): The unique identifier of the bidder making the offer.

    """

    def __init__(self, identifier: int, amount: float, offer_date: datetime, auction_id: int, bidder_id: int):
        """
        Initializes an Offer object with the provided attributes.

        Args:
            identifier (int): The unique identifier of the offer.
            amount (float): The amount of the offer.
            offer_date (datetime): The date and time when the offer was made.
            auction_id (int): The unique identifier of the auction associated with the offer.
            bidder_id (int): The unique identifier of the bidder making the offer.

        """

        super().__init__(identifier)
        self.amount = amount
        self.offer_date = offer_date
        self.auction_id = auction_id
        self.bidder_id = bidder_id
