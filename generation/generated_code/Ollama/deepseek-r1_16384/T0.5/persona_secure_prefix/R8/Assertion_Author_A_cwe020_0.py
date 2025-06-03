import re


def match_string(target_string):
    return bool(re.fullmatch(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$", target_string))


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
    parts = target_string.split(".")
    if len(parts) != 3:
        return False
    for part in parts:
        if not part:
            return False
    return True
