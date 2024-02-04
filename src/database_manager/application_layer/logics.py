"""
Utility Module

This module provides utility functions for data validation and file handling.

Functions:
    validate_input: Validates user input based on the expected data type.
    retype_data: Retypes data from XML for database insertion.
    load_xml: Loads XML data and parses it into element name and data.
    load_file: Loads text data from a file.

Exceptions:
    InvalidFileSuffixError: Raised when an unexpected file suffix is encountered.

"""


from datetime import datetime


class InvalidFileSuffixError(Exception):
    """
    Exception for unexpected file suffix.

    """

    def __init__(self, suffix):
        """
        Initializes the InvalidFileSuffixError with the unexpected file suffix.

        Args:
            suffix (str): The unexpected file suffix.

        """

        self.message = f'Unexpected file suffix, expected "{suffix}"'
        super().__init__(self.message)


def validate_input(typeof, user_data):
    """
    Validates user input based on the expected data type.

    Args:
        typeof (type): The expected data type.
        user_data (str): The user-provided data.

    Returns:
        Any: The converted user input.

    """

    if user_data == '':
        return

    if typeof is datetime:
        user_data = user_data.replace('.', '-').replace('/', '-')
        if len(user_data) > 10:
            converted_input = datetime.strptime(user_data, '%Y-%m-%d %H:%M:%S')
        else:
            converted_input = datetime.strptime(user_data, '%Y-%m-%d')
    else:
        if typeof is int:
            user_data = user_data.replace(' ', '')
        converted_input = typeof(user_data)
    return converted_input


def retype_data(element_data, params):
    """
    Retypes data from XML for database insertion.

    Args:
        element_data (list): The data extracted from XML.
        params (dict): The parameters of the database entity.

    Returns:
        list: The retyped data ready for insertion into the database.

    """

    retyped_data = []

    for row in element_data:
        object_data = {}
        for value in row:
            try:
                id_const = 'IDENTIFIER'
                row[value] = row[value].strip()
                if row[value].lower() == 'none' or row[value].lower() == 'null':
                    retyped_value = None
                else:
                    retyped_value = params[value.lower() if value != 'ID' else id_const.lower()](row[value])
                object_data[value.lower() if value != 'ID' else id_const.lower()] = retyped_value
            except:
                raise Exception('Data are not in format of database table')
        retyped_data.append(object_data)

    return retyped_data


def load_xml(xml_string):
    """
    Loads XML data and parses it into element name and data.

    Args:
        xml_string (ElementTree): The XML data.

    Returns:
        tuple: A tuple containing the element name and the data extracted from XML.

    """

    element_name = None
    element_data = []

    for index, data in enumerate(xml_string.findall('./*')):
        if index == 0:
            element_name = data.tag
        if element_name != data.tag:
            raise Exception('Import data are not consistent')
        row_data = {}
        for child in data:
            row_data[child.tag] = child.text
        element_data.append(row_data)

    return element_name, element_data


def load_file(path, suffix):
    """
    Loads text data from a file.

    Args:
        path (str): The path to the file.
        suffix (str): The expected file suffix.

    Returns:
        str: The text data from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the program does not have permissions to access the file.
        OSError: If there is an OS-related problem loading the file.
        InvalidFileSuffixError: If the file has an unexpected suffix.
        Exception: For any other unknown problem loading the file.

    """

    path = path.replace('\'', '')
    try:
        if not path.endswith(suffix):
            raise InvalidFileSuffixError(suffix)

        with open(path, 'r') as file:
            xml_text = file.read()

        return xml_text
    except FileNotFoundError:
        raise Exception(f'File "{path}" does not exist')
    except PermissionError:
        raise Exception(f'Program does not have permissions to work with file "{path}"')
    except OSError:
        raise Exception(f'OS problem loading file "{path}"')
    except InvalidFileSuffixError as e:
        raise Exception(str(e))
    except Exception:
        raise Exception(f'Unknown problem appeared loading file "{path}"')
