import re

def match_string(target_string):
    """
    Check if the input string is in the format 'x.y.z', where x, y, z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = re.compile(r'^\d\.\d\.\d$')  # Regular expression for 'x.y.z' format
    return bool(pattern.match(target_string))