import re

def match_string(target_string):
    pattern = r'\D+\d+\.\D+'  # Regular expression to match "x.y.z" format
    return bool(re.match(pattern, target_string))  # Check if the string matches the regular expression