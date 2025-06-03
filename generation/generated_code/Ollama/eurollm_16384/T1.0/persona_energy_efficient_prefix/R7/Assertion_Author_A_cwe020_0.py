import re


def match_string(target_string):
    """
    Check if the input string is a valid string in the format 'x.y.z',
    where x, y and z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    # Regex pattern to match 'x.y.z' format where x, y, and z are strings
    pattern = r'(?:[a-zA-Z][\w\-\.\s]{1,}|(.))"' * 3
    match_object = re.fullmatch(pattern, target_string)
    return match_object is not None
