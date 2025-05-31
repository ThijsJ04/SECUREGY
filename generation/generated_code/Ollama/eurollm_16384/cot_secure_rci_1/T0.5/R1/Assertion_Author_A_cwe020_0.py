import re

def match_string(target_string):
    '''
    Check if the input string is a valid string with the format x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
    pattern = r'(\w).*?(\w).*?(\w)'  # Regular expression pattern: (\w) matches one word character, .*? allows for a non-greedy match of any characters (including spaces), and \w again matches one word character. This pattern ensures that the input string has three parts separated by dots
    if re.match(pattern, target_string):  # Check if the input string matches the pattern using the re.match function
        return True
    else:
        return False