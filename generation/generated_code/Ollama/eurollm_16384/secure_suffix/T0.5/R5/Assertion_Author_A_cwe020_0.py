import re

def match_string(target_string):
    pattern = r'.*?(x\.)(.*?)(y\.)(.*?)(z)(\w+)'
    match = re.match(pattern, target_string)
    if match:
        return True
    else:
        return False