import re


def match_string(target_string):
    pattern = r"[a-zA-Z]+(?:\.[a-zA-Z]+)+$"
    return bool(re.match(pattern, target_string))


# Test the function
print(match_string("x.y.z"))  # Expected output: True
print(match_string("x"))  # Expected output: False
