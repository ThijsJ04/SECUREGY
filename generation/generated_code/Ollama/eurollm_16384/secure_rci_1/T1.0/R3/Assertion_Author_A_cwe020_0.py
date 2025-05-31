import re

def match_string(target_string):
    pattern = r'\d+(\.\d+)*$'  # Match one or more digits, followed by zero or more decimal points and digits, then end of line
    return bool(re.match(pattern, target_string))

print(match_string('x.y.z'))   # True
print(match_string('x'))      # False