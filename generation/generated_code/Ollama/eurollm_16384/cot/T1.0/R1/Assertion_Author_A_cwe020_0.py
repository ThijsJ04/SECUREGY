import re

def match_string(target_string):
    pattern = r'\d.\d.\d'
    return bool(re.match(pattern, target_string))

print(match_string('x.y.z'))  # Output: True
print(match_string('x'))       # Output: False