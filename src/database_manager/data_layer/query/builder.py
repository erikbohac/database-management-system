"""
Query Builder

This module provides a class for dynamically constructing SQL queries based on object attributes.

Classes:
    QueryBuilder: A class for dynamically constructing SQL queries.

"""


class QueryBuilder:
    """
    A class for dynamically constructing SQL queries based on object attributes.

    Methods:
        get_schema(data: object) -> tuple: Extracts the schema information from the given object.
        get_schema_values(data: list) -> list: Extracts the schema values from a list of objects.
        create_import_insert(data: list) -> tuple: Creates an import insert query for a list of objects.
        create_insert(data: object) -> tuple: Creates an insert query for a single object.
        create_delete(data: object) -> tuple: Creates a delete query for a single object.
        create_select(data: object) -> tuple: Creates a select query for a single object.
        create_update(data: object) -> tuple: Creates an update query for a single object.
        id_is_not_null(values: list, id_index: int) -> bool: Checks if the ID attribute is not null.
        are_not_all_none(values: list, id_index: int) -> bool: Checks if at least one attribute (except ID) is not null.

    """

    def __init__(self):
        """
        Initializes the QueryBuilder instance.

        """

        pass

    def get_schema(self, data: object):
        """
        Extracts the schema information from the given object.

        Args:
            data (object): The object from which to extract schema information.

        Returns:
            tuple: A tuple containing the object name, attribute names (keys), and attribute values.

        """

        name = type(data).__name__.upper()
        params = vars(data)
        keys = [key.upper() for key in params.keys()]
        values = list(params.values())
        return name, keys, values

    def get_schema_values(self, data: list):
        """
        Extracts the schema values from a list of objects.

        Args:
            data (list): A list of objects from which to extract schema values.

        Returns:
            list: A list containing the schema values for each object in the input list.

        """

        final_vals = []
        for value in data:
            params = vars(value)
            final_vals.append(list(params.values()))
        return final_vals

    def create_import_insert(self, data: list):
        """
        Creates an import insert query for a list of objects.

        Args:
            data (list): A list of objects for which to create the import insert query.

        Returns:
            tuple: A tuple containing the import insert query and the corresponding values.

        Raises:
            Exception: If at least one value must be not null in each object.

        """

        name, keys, _ = self.get_schema(data[0])
        values = self.get_schema_values(data)
        id_index = keys.index('ID')

        for value in values:
            if not self.id_is_not_null(value, id_index) and not self.are_not_all_none(value, id_index):
                raise Exception('At least one value must be not null in each object')

        query = f'INSERT INTO {name}({", ".join(key for key in keys)}) VALUES ({", ".join("%s" for _ in keys)});'

        return query, values

    def create_insert(self, data: object):
        """
        Creates an insert query for a single object.

        Args:
            data (object): The object for which to create the insert query.

        Returns:
            tuple: A tuple containing the insert query and the corresponding values.

        Raises:
            Exception: If at least one value must be not null.

        """

        name, keys, values = self.get_schema(data)
        id_index = keys.index('ID')

        if not self.are_not_all_none(values, id_index):
            raise Exception('At least one value must be not null')

        query = f'INSERT INTO {name}({", ".join(keys[index] for index in range(len(keys))if index != id_index)}) VALUES ({", ".join("%s" for index in range(len(keys)) if index != id_index)});'
        values = [values[index] for index in range(len(values)) if index != id_index]

        return query, values

    def create_delete(self, data: object):
        """
        Creates a delete query for a single object.

        Args:
            data (object): The object for which to create the delete query.

        Returns:
            tuple: A tuple containing the delete query and the corresponding values.

        Raises:
            Exception: If at least one value must be not null.

        """

        name, keys, values = self.get_schema(data)
        id_index = keys.index('ID')

        if not self.id_is_not_null(values, id_index) and not self.are_not_all_none(values, id_index):
            raise Exception('At least one value must be not null')

        query = f'DELETE FROM {name} WHERE {" AND ".join(keys[index] + " = %s" for index in range(len(keys)) if values[index] is not None)};'
        values = [value for value in values if value is not None]

        return query, values

    def create_select(self, data: object):
        """
        Creates a select query for a single object.

        Args:
            data (object): The object for which to create the select query.

        Returns:
            tuple: A tuple containing the select query and the corresponding values.

        """

        name, keys, values = self.get_schema(data)
        id_index = keys.index('ID')

        if not self.id_is_not_null(values, id_index) and not self.are_not_all_none(values, id_index):
            query = f'SELECT * FROM {name};'
        else:
            query = f'SELECT * FROM {name} WHERE {" AND ".join(keys[index] + " = %s" for index in range(len(keys)) if values[index] is not None)};'
        values = [value for value in values if value is not None]

        return query, values

    def create_update(self, data: object):
        """
        Creates an update query for a single object.

        Args:
            data (object): The object for which to create the update query.

        Returns:
            tuple: A tuple containing the update query and the corresponding values.

        Raises:
            Exception: If the ID attribute must be a number 0 or higher, or if at least one attribute (except ID) must be not null.

        """

        name, keys, values = self.get_schema(data)
        id_index = keys.index('ID')

        if not self.id_is_not_null(values, id_index):
            raise Exception('ID must be number 0 or higher')

        if not self.are_not_all_none(values, id_index):
            raise Exception('At least one value except ID must be not null')

        query = f'UPDATE {name} SET {", ".join(keys[index] + " = %s" for index in range(len(keys)) if index != id_index and values[index] is not None)} WHERE ID = %s;'
        values = [value for value in values if value is not None]
        values.append(values.pop(0))

        return query, values

    def id_is_not_null(self, values: list, id_index: int):
        """
        Checks if the ID attribute is not null.

        Args:
            values (list): A list of attribute values.
            id_index (int): The index of the ID attribute.

        Returns:
            bool: True if the ID attribute is not null and greater than or equal to 0, False otherwise.

        """

        if values[id_index] is None:
            return False
        if values[id_index] < 0:
            return False
        return True

    def are_not_all_none(self, values: list, id_index: int):
        """
        Checks if at least one attribute (except ID) is not null.

        Args:
            values (list): A list of attribute values.
            id_index (int): The index of the ID attribute.

        Returns:
            bool: True if at least one attribute (except ID) is not null, False otherwise.

        """

        is_not_none = False
        for val in range(len(values)):
            if id_index == val:
                continue
            if values[val] is not None:
                is_not_none = True

        return is_not_none
