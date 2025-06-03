import re


def match_string(target_string):
    """
    Check if the input string is valid with the following format: x.y.z (where x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = r"^[a-zA-Z]+(.[a-zA-Z]+)*[0-9]+$"
    return bool(re.match(pattern, target_string))
