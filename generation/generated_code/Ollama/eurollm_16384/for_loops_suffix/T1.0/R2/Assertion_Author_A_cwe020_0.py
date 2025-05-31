import re

def match_string(target_string):
    pattern = r'^x\.(y|z)$'
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False

# Test the function
print(match_string('x.y.z'))   # Expected output: True
print(match_string('x'))       # Expected output: False