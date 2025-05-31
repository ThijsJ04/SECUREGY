import re

def match_string(target_string):
    '''
    Check if the input string is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
    if not isinstance(target_string, str):
        return False
    # Check for leading or trailing whitespace
    if target_string.strip() != target_string:
        return False
    parts = target_string.split('.')
    if len(parts) != 3:
        return False
    for part in parts:
        if not part:  # Empty string after split is invalid
            return False
    return True