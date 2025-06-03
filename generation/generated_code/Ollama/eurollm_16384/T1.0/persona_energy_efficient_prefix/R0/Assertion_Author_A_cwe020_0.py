import re


def match_string(target_string):
    """
    Check if the input string is a valid string with the format: x.y.z where x, y, z are strings

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = r"(\D)(.*?)\1"
    match = re.search(pattern, target_string)
    return bool(match) and (len(match.group(2)) == 3)
