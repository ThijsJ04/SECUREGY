import re

def match_string(target_string):
    """Check if the input string is a valid string with the format x.y.z where x, y, and z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    if not re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string):
        return False
    parts = target_string.split('.')
    for i in range(len(parts) - 1, -1, -1):
        part = parts[i]
        if not re.match(r'^[a-zA-Z0-9]+$', part):
            return False
    return True