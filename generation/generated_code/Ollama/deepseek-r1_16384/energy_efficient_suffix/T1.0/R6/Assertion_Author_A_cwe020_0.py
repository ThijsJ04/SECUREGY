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
    # Check if there are exactly two '.' in the string
    if target_string.count('.') != 2:
        return False
    # Split the string by '.' and check resulting parts
    parts = target_string.split('.')
    # Must have exactly three non-empty parts
    if len(parts) != 3 or any(not part for part in parts):
        return False
    return True

# Example usage (for testing purposes)
print(match_string('x.y.z'))  # Output: True
print(match_string('x'))      # Output: False