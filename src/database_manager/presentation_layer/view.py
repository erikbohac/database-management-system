"""
Utility Functions

This module provides utility functions for formatting text and generating tables.

Functions:
    outline_text(message: str, length: int): Creates a bordered text block.
    reformat_console_text(console: str, subdir: list): Reformat the console prompt with a subdirectory.
    generate_text_table(headers: list, data: list): Generates a text-based table.
    replace_chars(text: str): Replaces specific characters in a string.

"""


def outline_text(message: str, length: int):
    """
    Creates a bordered text block.

    Args:
        message (str): The message to be enclosed within the border.
        length (int): The length of the border.

    Returns:
        str: The bordered text block.

    """

    line_char = '='
    output = ''

    for _ in range(length):
        output += line_char
    output += f'\n{message}\n'
    for _ in range(length):
        output += line_char

    return output


def reformat_console_text(console: str, subdir: list):
    """
    Reformat the console prompt with a subdirectory.

    Args:
        console (str): The original console prompt.
        subdir (list): A list of strings representing the subdirectory.

    Returns:
        str: The reformatted console prompt.

    """

    console_parts = console.split('~')
    new_console = f'{console_parts[0]}~('
    new_console += '-'.join(subdir).upper()
    new_console += f'){console_parts[1]}'
    return new_console


def generate_text_table(headers: list, data: list):
    """
    Generates a text-based table.

    Args:
        headers (list): A list of strings representing table headers.
        data (list): A list of lists representing table data.

    Returns:
        tuple: A tuple containing the text-based table and its total width.

    """

    column_widths = []
    for column in zip(headers, *data):
        max_length = max(len(str(item)) for item in column)
        column_widths.append(max_length)

    header_row_parts = []
    for header, width in zip(headers, column_widths):
        header_row_parts.append(str(header).ljust(width))
    header_row = " | ".join(header_row_parts)

    separator_row_parts = []
    for index in range(len(column_widths)):
        separator_row_parts.append("-" * column_widths[index])
    separator_row = "-|-".join(separator_row_parts)

    data_rows = []
    for row in data:
        row_parts = []
        for item, width in zip(row, column_widths):
            row_parts.append(str(item).ljust(width))
        data_rows.append(" | ".join(row_parts))

    table_parts = [header_row, separator_row, *data_rows]
    table = "\n".join(table_parts)

    total_width = sum(column_widths) + (len(column_widths) - 1) * 3
    return table, total_width


def replace_chars(text):
    """
    Replaces specific characters in a string.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: The processed text with characters replaced.

    """

    text = text.replace('_', ' ')
    text = text.replace('DATETIME.DATETIME', 'YYYY/MM/DD HH/MM/SS')
    text = text.replace('AUCTIONTYPE', 'PUBLIC/ANONYMOUS')
    text = text.replace('BOOL', 'TRUE/FALSE')
    return text
