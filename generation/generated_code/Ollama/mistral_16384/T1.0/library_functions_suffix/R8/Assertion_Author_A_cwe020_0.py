from re import match, pattern


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
    pattern = r"^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"  # Checks for any alphanumeric characters with optional dots between them. The ^ and $ symbols anchor the pattern to the start and end of the string respectively, ensuring it matches only full strings
    if match(pattern, target_string):
        return True
    else:
        return False
