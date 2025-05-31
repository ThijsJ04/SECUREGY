import re

def match_string(target_string):
    pattern = r'.*'  # Allow leading or trailing whitespace
    if len(target_string) != 3:
        return False
    for char in target_string:
        try:
            digit = int(char)
            if digit < 0 or digit > 9:
                return False
        except ValueError:
            return False  # Character is not a digit or dot
    return True