import re

def match_string(target_string):
    """
    Check if the input string is in the valid format 'x.y.z' 
    where x, y, and z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    # Use a regular expression to check for the format 'x.y.z'
    return bool(re.match(r'\d+\.\d+\.\d+', target_string))