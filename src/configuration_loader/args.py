"""
Argument Parser

This module provides a function for creating an argument parser for database management.

Functions:
    arguments(): Creates an argument parser for database management.

"""


import argparse


def arguments():
    """
    Creates an argument parser for database management.

    Returns:
        argparse.ArgumentParser: An argument parser object configured for database management.

    """

    info = 'Program used for database management, run trough command "python main.py"'
    parser = argparse.ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter, description=info)

    return parser
