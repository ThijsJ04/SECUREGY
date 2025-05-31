import re

def match_string(target_string):
    pattern = r'\d+\.\d+\.\d+'  # Regular expression pattern for three digits separated by dots
    return bool(re.match(pattern, target_string))

# Example usage:
print(match_string('x.y.z'))   # Returns True
print(match_string('x'))       # Returns False