import re


def match_string(target_string):
    """
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = r"^[a-zA-Z\s]+$"  # Match one or more alphanumeric characters and at most one whitespace character at the end
    if not re.match(pattern, target_string):
        return False

    x, y, z = target_string.partition(".")
    if len(target_string) != 3:
        return False
    if x and not isinstance(x, str):
        return False
    if y and not isinstance(y, str):
        return False
    if z and not isinstance(z, str):
        return False

    return True
