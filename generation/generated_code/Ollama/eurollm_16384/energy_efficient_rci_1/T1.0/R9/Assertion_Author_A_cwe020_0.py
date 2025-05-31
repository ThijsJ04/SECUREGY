import re

def match_string(target_string):
    '''
    Check if the input string is in the valid format x.y.z (x, y, z are strings).

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
    pattern = re.compile(r'\D.*?\d')  # Regular expression pattern to match any non-digit character followed by a digit
    if not target_string or not re.match(pattern, target_string):
        return False
    _, x, _, y, z = target_string.split('.', 4)
    try:
        assert len(x) == len(y) and len(y) == len(z), f'All three strings must have the same length.'
    except AssertionError as e:
        return False
    return True