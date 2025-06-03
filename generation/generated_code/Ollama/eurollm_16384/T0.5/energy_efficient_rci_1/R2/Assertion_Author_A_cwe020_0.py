import re


def match_string(target_string):
    """
    Check if the input string is in the format x.y.z where x, y, and z are strings.

    Args:
        target_string (str): The string to be checked.

    Returns:
        bool: True if the string is valid, False otherwise.

    Examples:
        >>> match_string('x.y.z')
        True
        >>> match_string('x')
        False
    """
    pattern = r"^[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]$"
    return bool(re.match(pattern, target_string))
