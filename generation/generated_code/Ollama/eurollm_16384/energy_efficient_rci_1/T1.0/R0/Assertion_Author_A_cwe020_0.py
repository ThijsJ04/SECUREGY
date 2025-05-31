import re

def match_string(target_string):
    pattern = r'\D+(\d+).*'
    return bool(re.match(pattern, target_string)) and len(re.split('\\D', target_string)[0]) == 3