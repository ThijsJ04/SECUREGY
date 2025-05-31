import re

def match_string(target_string):
    pattern = r'.*?[0-9]+\.[0-9]+\.[0-9]+$'
    return bool(re.match(pattern, target_string))

# Example usage:
print(match_string('x.y.z'))  # Returns True
print(match_string('x'))       # Returns False