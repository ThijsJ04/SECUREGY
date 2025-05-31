import re

def match_string(target_string):
    pattern = r'.*?x\.(.*?)z'  # Matches any characters before and after 'x', then captures the group between 'x' and '.' and another group between '.' and 'z'
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False