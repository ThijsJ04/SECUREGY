import re

def match_string(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    '''

    # Ensure that the input has the required format
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'  # Matches string with or without dots
    if not re.match(pattern, target_string):
        return False

    # Split the input into segments by dots
    segments = target_string.split('.')

    # Check each segment is a valid string (alphanumeric)
    for seg in segments:
        if not seg or not re.match(r'[a-zA-Z0-9]+', seg):
            return False

    return True