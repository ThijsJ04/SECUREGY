import re


def match_string(target_string):
    """
    Check if the input string is in the format x.y.z, where each part is a string.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = re.compile(r"^(\w+)\.(\w+)\.(\w+)", re.IGNORECASE)
    return bool(pattern.match(target_string))
