import re

def match_string(target_string):
    """
    Check if the input string is in the format x.y.z (where x, y, z are strings).

    :param target_string: The string to be checked.
    :return: True if the string matches the format, False otherwise.

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    # Use a regular expression pattern that matches one dot and then three more strings
    pattern = r'.*?(\w+).(.*?)\1'

    if not re.match(pattern, target_string):
        return False

    # Check if the string has exactly 3 parts separated by dots (assuming x.y.z)
    # However, this will also match strings like a.b and a.b.c. So, we need to verify manually here
    parts = target_string.split('.')
    if len(parts) != 3:
        return False

    for part in parts:
        if not isinstance(part, str):
            return False

    return True