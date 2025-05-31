import re

def match_string(target_string):
    # Check if the input string is of the correct length
    if len(target_string) != 3 or not target_string[0].isalpha() or not target_string[-1].isalpha():
        return False

    # Check that the middle character is a dot (".")
    pattern = r'.*'
    if re.match(pattern, target_string) == None: 
        return False

    return True