import re

def match_string(target_string):
    pattern = r"^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"
    return bool(re.match(pattern, target_string))