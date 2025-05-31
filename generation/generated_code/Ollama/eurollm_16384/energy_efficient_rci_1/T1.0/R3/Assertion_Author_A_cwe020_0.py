import re

def match_string(target_string):
    '''
    Check if the input string matches the format x.y.z where each substring is a string.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
    pattern = r"[a-zA-Z\s]+."
    if re.match(pattern, target_string):
        return len(re.split("[.]", target_string)) == 3
    else:
        return False