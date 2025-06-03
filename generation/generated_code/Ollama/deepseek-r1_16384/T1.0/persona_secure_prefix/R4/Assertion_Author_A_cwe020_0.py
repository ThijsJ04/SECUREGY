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
    # Split the target string by '.' and check if it results in exactly three non-empty parts
    parts = target_string.split(".")
    if len(parts) != 3:
        return False
    for part in parts:
        if not part:  # Check that each part is not empty
            return False
    return True


def match_string(target_string):
    import re

    pattern = r"^([^.]+)\.([^.]+)\.([^.]+)$"
    return bool(re.fullmatch(pattern, target_string))
