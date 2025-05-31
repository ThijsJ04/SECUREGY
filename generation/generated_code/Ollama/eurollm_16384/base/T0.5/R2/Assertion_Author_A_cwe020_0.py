import re

def match_string(target_string):
    pattern = r'.*?(\d+).*?(\d+).*?'
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False