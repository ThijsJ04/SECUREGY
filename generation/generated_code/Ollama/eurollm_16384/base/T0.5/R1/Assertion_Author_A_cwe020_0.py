import re

def match_string(target_string):
    pattern = r'.*?(\d+)\.(\d+)\.(\d+)$'
    match = re.fullmatch(pattern, target_string)
    if match:
        return True
    else:
        return False