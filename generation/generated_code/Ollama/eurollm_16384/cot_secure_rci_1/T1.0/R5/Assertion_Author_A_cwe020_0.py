import re

def match_string(target_string):
    pattern = r'.*?(\w+)\.(\w+)(\.\w+)'  # This is a regex pattern to match x.y.z format
    match = re.search(pattern, target_string)
    return bool(match and len(match.groups()) == 3 and all(isinstance(g, str) for g in match.groups()))