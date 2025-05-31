import re

def match_string(target_string):
    """
    Check if the input string is in the valid format 'x.y.z', where x, y, and z are strings.

    Args:
        target_string (str): The string to be checked.

    Returns:
        bool: True if the string is valid, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> match_string('x.y.z')
        True
        >>> match_string('x')
        False
    """
    pattern = r'^[a-zA-Z0-9.]+\.[a-zA-Z0-9.]+$'  # regular expression pattern to match the input string
    if not isinstance(target_string, str):
        raise TypeError("Input must be a string")
    return bool(re.match(pattern, target_string))