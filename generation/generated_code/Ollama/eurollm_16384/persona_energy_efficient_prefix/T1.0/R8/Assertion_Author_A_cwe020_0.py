import re

def match_string(target_string):
    pattern = r'\D*(\w+).*?(\d+\.\d+|\d+\.\d+)[.]\1'
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False