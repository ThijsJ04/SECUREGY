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
    # Check if the string matches the pattern of three non-empty parts separated by dots
    return bool(re.fullmatch(r"\S+\.\S+\.\S+", target_string))
