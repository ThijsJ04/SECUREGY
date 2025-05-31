import re

def match_string(target_string):
    """
    Checks if the input string is in the format x.y.z where x, y, and z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = r'^[a-zA-Z]+.[a-zA-Z]+.[a-zA-Z]+$'  # Regular expression to match the format
    if re.match(pattern, target_string):
        return True
    else:
        return False