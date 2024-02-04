"""
Configuration Loader

This module provides a class for loading configuration settings from a file using the configparser module.

Classes:
    ConfigLoader: A class for loading configuration settings from a file.

"""


import configparser


class ConfigLoader:
    """
    A class for loading configuration settings from a file.

    Attributes:
        path (str): The path to the configuration file.

    Methods:
        load_config(): Loads configuration settings from the specified file and returns them as a list.

    """

    def __init__(self, path):
        """
        Initializes the ConfigLoader instance with the path to the configuration file.

        Args:
            path (str): The path to the configuration file.

        """

        self.path = path

    def load_config(self):
        """
        Loads configuration settings from the specified file and returns them as a list.

        Returns:
            tuple: A tuple containing configuration data (IP address, port, user, password, database name,
                   connection attempts, timeout, import file) and additional information (database name, log file).

        Raises:
            TypeError: If the configuration data types are invalid.

        """

        config = configparser.ConfigParser()
        config.read(self.path)

        ip = config['CONNECTION']['IP_Address']
        port = config['CONNECTION']['Port']
        attempts = config['CONNECTION']['Attempt_Count']
        timeout = config['CONNECTION']['Timeout']
        user = config['DATABASE']['User']
        password = config['DATABASE']['Password']
        name = config['DATABASE']['Name']
        import_file = config['IMPORT']['XML_File']
        logs = config['LOG']['Log_File']

        try:
            attempts = int(attempts)
            timeout = int(timeout)
        except:
            raise TypeError('Invalid config data types')

        data_list = [ip, port, user, password, name, attempts, timeout, import_file]
        return data_list, name, logs
