import re

def match_string(target_string):
    # Check if target string is of length 3 and contains only alphanumeric characters
    pattern = r'^[a-zA-Z0-9]+$'
    if not re.match(pattern, target_string):
        return False

    # Split the target string into three parts at the '.' character
    parts = target_string.split('.')
    if len(parts) != 3:
        return False

    # Check if each part is a string of length greater than 0 and contains only alphanumeric characters
    for i in range(3):
        part = parts[i]
        if not re.match(r'^[a-zA-Z0-9]+$', part):
            return False
        if len(part) == 0:
            return False

    return True