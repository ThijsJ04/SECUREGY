import re


def match_string(target_string):
    pattern = r".*?(\d+).*?(\d+).*?(\d+)"
    match = re.match(pattern, target_string)
    return bool(match and len(match.groups()) == 3)


# Example usage:
print(match_string("x.y.z"))  # True
print(match_string("x"))  # False
