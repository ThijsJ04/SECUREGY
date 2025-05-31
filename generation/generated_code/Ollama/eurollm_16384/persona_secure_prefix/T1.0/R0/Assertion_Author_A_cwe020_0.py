import re

def match_string(target_string):
    pattern = r'\d+.\d+.\d+'  # Regular expression pattern for valid string format
    if re.match(pattern, target_string):
        return True
    else:
        return False