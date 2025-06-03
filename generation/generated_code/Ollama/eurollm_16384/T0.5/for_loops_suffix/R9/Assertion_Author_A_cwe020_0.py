import re


def match_string(target_string):
    """
    Check if the input string is in the format 'x.y.z' where x, y, and z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = r".+?(\\d+\\.\\d+\\.\\d+)"  # Regular expression pattern to match the format 'x.y.z'
    match = re.search(pattern, target_string)
    return bool(match) and len(match.groups()) == 3
