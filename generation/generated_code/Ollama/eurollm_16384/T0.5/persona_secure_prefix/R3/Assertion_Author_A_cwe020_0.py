import re


def match_string(target_string):
    """
    Check if the input string is in the format x.y.z, where x, y, and z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    """
    pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$"
    return bool(re.match(pattern, target_string))
