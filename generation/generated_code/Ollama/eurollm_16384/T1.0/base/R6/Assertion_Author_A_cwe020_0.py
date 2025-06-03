import re


def match_string(target_string):
    pattern = r".+\\x"
    match = re.fullmatch(pattern, target_string)
    return bool(match)


# Test cases from the original prompt
print(match_string("x.y.z"))  # Expected output: True
print(match_string("x"))  # Expected output: False
