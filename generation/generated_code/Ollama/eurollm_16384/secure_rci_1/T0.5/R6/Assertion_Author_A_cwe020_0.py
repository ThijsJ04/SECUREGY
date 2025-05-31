import re

def match_string(target_string):
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+$'
    return bool(re.match(pattern, target_string))

# Example usage:
print(match_string('x.y.z'))  # True
print(match_string('x'))       # False