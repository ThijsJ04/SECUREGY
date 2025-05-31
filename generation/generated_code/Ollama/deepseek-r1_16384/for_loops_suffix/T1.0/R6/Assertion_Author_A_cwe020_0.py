import re

def match_string(target_string):
    '''
    Check if the input string is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
    # Split the target string by '.' into parts
    parts = target_string.split('.')

    # Check if there are exactly 3 parts
    if len(parts) == 3:
        return True
    else:
        return False