import re

def match_string(target_string):
    # Check if target string is of length 3
    if len(target_string) != 3:
        return False

    # Attempt to unpack the target string into three strings (x, y, z)
    try:
        a, b, c = target_string.split('.')
    except ValueError:  # If target string cannot be split by '.'
        return False

    # Check if all three strings are non-empty
    if not a or not b or not c:
        return False

    return True