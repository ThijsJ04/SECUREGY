import re


def match_string(target_string):
    """
    Check if the input string is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    # Check if there are exactly two dots in the string
    if target_string.count(".") != 2:
        return False
    # Split the string into three parts based on the dots
    parts = target_string.split(".")
    # Ensure all three parts are non-empty strings
    for part in parts:
        if not part:
            return False
    return True
