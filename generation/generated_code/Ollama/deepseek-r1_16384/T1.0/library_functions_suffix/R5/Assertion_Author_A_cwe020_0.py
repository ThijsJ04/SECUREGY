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
    # Use regex to check for exactly three components separated by periods
    pattern = r"^\w+\.\w+\.\w+$"
    return bool(re.fullmatch(pattern, target_string))
