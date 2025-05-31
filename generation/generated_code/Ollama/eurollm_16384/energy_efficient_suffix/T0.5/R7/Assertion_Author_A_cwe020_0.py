import re

def match_string(target_string):
    pattern = r'\D+?[xyz]\D+?'  # Match one of x, y or z followed by optional non-digit characters and another digit
    return bool(re.match(pattern, target_string))