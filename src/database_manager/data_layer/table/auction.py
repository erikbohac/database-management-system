"""
Auction Module

This module defines the Auction class and AuctionType enum for managing auctions.

Classes:
    AuctionType: An enumeration representing the type of auction.
    Auction: A class representing an auction entity.

"""


from datetime import datetime
from enum import Enum
from .database_entity import DatabaseEntity


class AuctionType(Enum):
    """
    An enumeration representing the type of auction.

    Attributes:
        PUBLIC (str): Public auction type.
        ANONYMOUS (str): Anonymous auction type.

    """

    PUBLIC = 'PUBLIC'
    ANONYMOUS = 'ANONYMOUS'


class Auction(DatabaseEntity):
    """
    A class representing an auction entity.

    Attributes:
        identifier (int): The unique identifier of the auction.
        start_date (datetime): The start date and time of the auction.
        end_date (datetime): The end date and time of the auction.
        auction_type (AuctionType): The type of the auction (public or anonymous).
        auction_description (str): A description of the auction.
        item_id (int): The unique identifier of the item associated with the auction.

    """

    def __init__(self, identifier: int, start_date: datetime, end_date: datetime, auction_type: AuctionType, auction_description: str, item_id: int):
        """
        Initializes an Auction object with the provided attributes.

        Args:
            identifier (int): The unique identifier of the auction.
            start_date (datetime): The start date and time of the auction.
            end_date (datetime): The end date and time of the auction.
            auction_type (AuctionType): The type of the auction (public or anonymous).
            auction_description (str): A description of the auction.
            item_id (int): The unique identifier of the item associated with the auction.

        """

        super().__init__(identifier)
        self.start_date = start_date
        self.end_date = end_date
        self.auction_type = auction_type
        self.auction_description = auction_description
        self.item_id = item_id
