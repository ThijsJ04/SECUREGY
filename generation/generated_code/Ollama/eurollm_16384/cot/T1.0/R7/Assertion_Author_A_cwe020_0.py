import re

def match_string(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
    pattern = r'.*?(\D+).*?(\D+).*?(\D+)'  # Regular expression to split the string into three parts
    matches = re.match(pattern, target_string)
    if matches and len(matches.groups()) == 3:
        return all([isinstance(match, str) for match in matches.groups()])
    else:
        return False