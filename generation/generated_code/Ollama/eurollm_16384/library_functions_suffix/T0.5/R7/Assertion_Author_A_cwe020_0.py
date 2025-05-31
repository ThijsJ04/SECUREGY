import re

def match_string(target_string):
    pattern = r'.*?[xyz].*?'
    match = re.fullmatch(pattern, target_string)
    return bool(match)

# Example usage:
print(match_string('x.y.z'))   # True
print(match_string('x'))       # False