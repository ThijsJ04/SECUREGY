import re

def match_string(target_string):
    '''
    Check if the input string is in the valid format of x.y.z (x, y, z being strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    '''
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$|^[a-zA-Z0-9]+([.][a-zA-Z0-9]+)*$'
    return bool(re.match(pattern, target_string))