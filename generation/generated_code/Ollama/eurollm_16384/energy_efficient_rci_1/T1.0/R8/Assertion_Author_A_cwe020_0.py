import re

def match_string(target_string):
    pattern = r'\D+?\.\D+?'  # Matches one or more non-digit characters followed by a dot and then one or more non-digit characters
    return bool(re.match(pattern, target_string)) if re.search('\D', target_string) else False