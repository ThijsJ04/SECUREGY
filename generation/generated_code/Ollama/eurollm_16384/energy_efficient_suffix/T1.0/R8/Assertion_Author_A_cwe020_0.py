import re

def match_string(target_string):
    """
    Check if the input sting is a valid string with the following formats: x.y.z, x:y:z or /path/to/file

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    """
    patterns = [r'^x\.([a-zA-Z]+)\.([a-zA-Z]+)$', 
                r'^\d+\:\.\d+\:\.\d+$', 
                r'^/(\w+)(\:\.(\w+){0,})*\/?$']

    test_string = target_string.strip()  # remove leading and trailing spaces
    for pattern in patterns:
        if bool(re.match(pattern, test_string)):
            return True
    return False 

print(match_string('x.y.z')) # True
print(match_string('x')) # False