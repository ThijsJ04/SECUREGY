import re

def match_string(target_string):
    pattern = r'.*?(x.y.z)(\D)'  # x, y, z are strings with optional leading/trailing whitespace
    match = re.search(pattern, target_string)
    if match and (re.search('\s', match.group(2)) or re.search(r'\d', match.group(1))):  # check if x has numbers or spaces
        return False
    else:
        return True