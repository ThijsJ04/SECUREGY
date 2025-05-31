import re

def match_string(target_string):
    pattern = r"^[a-zA-Z]+\.[a-zA-Z]+[a-zA-Z]$"
    return bool(re.match(pattern, target_string))