import re

def match_string(target_string):
    pattern = r'\D+?(?=\D+|\d+)'
    return bool(re.match(pattern, target_string))

# Test cases
print(match_string('x.y.z'))  # True
print(match_string('x'))       # False