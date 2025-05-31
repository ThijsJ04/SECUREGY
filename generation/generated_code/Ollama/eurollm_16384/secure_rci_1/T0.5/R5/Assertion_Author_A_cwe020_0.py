import re

def match_string(target_string):
    pattern = r'.*?(\d+).(\d+).(\d+)'  # Regular expression pattern for x.y.z
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False