# Part IV - Dictionaries & Advanced Iteration

def create_dict(keys, values):
    """
    Create a dictionary from parallel lists of keys and values.

    Parameters:
        keys (list): List of keys
        values (list): List of values

    Returns:
        dict: Dictionary mapping keys to values
    """
<<<<<<< HEAD
    return dict(zip(keys, values))
=======

    return dict(zip(keys, values))

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def get_value(dct, key):
    """
    Retrieve a value from a dictionary by key.

    Parameters:
        dct (dict): The dictionary to search
        key (any): The key to look up

    Returns:
        any: The value associated with the key if found, otherwise None
    """
<<<<<<< HEAD
    return dct.get(key)

=======

    return dct.get(key)

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def set_value(dct, key, value):
    """
    Add or update a key-value pair in a dictionary.

    Parameters:
        dct (dict): The dictionary to modify
        key (any): The key to set
        value (any): The value to associate with the key

    Returns:
        dict: The modified dictionary
    """
<<<<<<< HEAD
    dct[key] = value
    return dct
=======

    dct[key] = value

    return dct

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def has_key(dct, key):
    """
    Check if a key exists in a dictionary.

    Parameters:
        dct (dict): The dictionary to search
        key (any): The key to check

    Returns:
        bool: True if key exists, False otherwise
    """
<<<<<<< HEAD
    return key in dct

=======

    return key in dct

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def get_keys(dct):
    """
    Get all keys from a dictionary.

    Parameters:
        dct (dict): The dictionary to query

    Returns:
        list: List of all keys
    """
<<<<<<< HEAD
    return list(dct.keys())
=======

    return list(dct.keys())

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def get_values(dct):
    """
    Get all values from a dictionary.

    Parameters:
        dct (dict): The dictionary to query

    Returns:
        list: List of all values
    """
<<<<<<< HEAD
    return list(dct.values())
=======

    return list(dct.values())

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def count_keys(dct):
    """
    Count the number of key-value pairs in a dictionary.

    Parameters:
        dct (dict): The dictionary to count

    Returns:
        int: Number of key-value pairs
    """
<<<<<<< HEAD
    return len(dct)
=======

    return len(dct)

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def remove_key(dct, key):
    """
    Remove a key-value pair from a dictionary.

    Parameters:
        dct (dict): The dictionary to modify
        key (any): The key to remove

    Returns:
        dict: The modified dictionary
    """
<<<<<<< HEAD
    if key in dct:
        del dct[key]
    return dct
=======

    if key in dct:
        del dct[key]

    return dct

    pass
>>>>>>> dd7ebeb51370a0b67088a1d0862c31862d845a6b

def iterate_list(lst, callback):
    """
    Apply a callback function to each element of a list.

    Parameters:
        lst (list): The list to iterate over
        callback (function): Function to apply to each element

    Returns:
        list: List containing the results from applying callback to each element
    """

    return [callback(item) for item in lst]

    pass

def find_item(lst, predicate):
    """
    Find the first item in a list that matches a condition.

    Parameters:
        lst (list): The list to search
        predicate (function): Function that returns True for matching items

    Returns:
        any: The first matching item if found, otherwise None
    """

    for item in lst:
        if predicate(item):
            return item
    return None

    pass