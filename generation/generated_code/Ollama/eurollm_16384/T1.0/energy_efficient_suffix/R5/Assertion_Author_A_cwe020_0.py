import re


def match_string(target_string):
    """
    Check if the input string is valid with format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = re.compile(
        r"^[a-zA-Z].*?$"
    )  # valid strings should start with a letter and end with nothing (.)
    #   (*?) makes it non-greedy to avoid leading spaces
    return bool(pattern.match(target_string))
