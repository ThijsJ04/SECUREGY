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
    # Check if the input is a string and matches the required pattern
    if not isinstance(target_string, str):
        return False
    pattern = r"^[^.]++\.[^.]++\.[^.]++$"
    return bool(re.fullmatch(pattern, target_string))
