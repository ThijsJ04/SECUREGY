import re


def match_string(target_string):
    pattern = r".*?(\d\.\d\.\d).*?"
    match = re.search(pattern, target_string)
    return bool(match) and len(match.groups()) == 1


# Test the function
print(match_string("x.y.z"))  # True
print(match_string("x"))  # False
