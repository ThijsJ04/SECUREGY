import re


def match_string(target_string):
    """
    Check if the input string is in the format x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = r"\d{1,3}\.\d{1,4}\.\d{1,4}"
    return bool(re.match(pattern, target_string))
