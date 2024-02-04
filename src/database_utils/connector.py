"""
MySQL Connector

This module provides a singleton class for establishing and managing MySQL connections.

Classes:
    Connector: A singleton class for establishing and managing MySQL connections.

"""


from mysql import connector


class Connector:
    """
    A singleton class for establishing and managing MySQL connections.

    Attributes:
        host (str): The hostname or IP address of the MySQL server.
        port (int): The port number of the MySQL server.
        user (str): The username for authentication.
        password (str): The password for authentication.
        name (str): The name of the MySQL database.
        attempts (int): The maximum number of connection attempts.
        timeout (int): The timeout for each connection attempt (in seconds).
        default_conf (tuple): A tuple containing default connection configuration
                              (host, port, user, password, name, timeout).
        connection: MySQL connection object.

    Methods:
        get_connection(): Establishes a MySQL connection.
        close_connection(): Closes the current MySQL connection.

    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Overrides the __new__ method to ensure only one instance of the class is created.

        Returns:
            obj: The instance of the class.

        """

        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host, port, user, password, name, attempts, timeout, default_conf=None):
        """
        Initializes the Connector instance with connection parameters.

        Args:
            host (str): The hostname or IP address of the MySQL server.
            port (int): The port number of the MySQL server.
            user (str): The username for authentication.
            password (str): The password for authentication.
            name (str): The name of the MySQL database.
            attempts (int): The maximum number of connection attempts.
            timeout (int): The timeout for each connection attempt (in seconds).
            default_conf (tuple): A tuple containing default connection configuration
                                  (host, port, user, password, name, timeout).

        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.name = name
        self.attempts = attempts
        self.timeout = timeout
        self.default_conf = default_conf
        self.connection = None

    def get_connection(self):
        """
        Establishes a MySQL connection.

        Returns:
            connection: A MySQL connection object.

        Raises:
            Exception: If connection fails after maximum attempts.

        """

        if self.connection is not None:
            return self.connection
        else:
            attempt = 0
            while attempt < self.attempts:
                try:
                    if self.connection is None:
                        self.connection = connector.connect(host=self.host,
                                                            port=self.port,
                                                            user=self.user,
                                                            password=self.password,
                                                            database=self.name,
                                                            connection_timeout=self.timeout)
                    else:
                        return self.connection
                except:
                    attempt += 1
            else:
                if self.default_conf is not None:
                    try:
                        self.connection = connector.connect(host=self.default_conf[0],
                                                            port=self.default_conf[1],
                                                            user=self.default_conf[2],
                                                            password=self.default_conf[3],
                                                            database=self.default_conf[4],
                                                            connection_timeout=self.default_conf[5])
                    finally:
                        if self.connection is not None:
                            return self.connection

    def close_connection(self):
        """
        Closes the current MySQL connection.

        """

        if self.connection is not None:
            self.connection.close()
