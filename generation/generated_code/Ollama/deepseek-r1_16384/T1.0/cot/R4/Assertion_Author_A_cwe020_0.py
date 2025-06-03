import re


def match_string(target_string):
    pattern = r"^([^.]+)\.([^.]+)\.([^.]+)$"
    return bool(re.fullmatch(pattern, target_string))


# Example usage:
# print(match_string('x.y.z'))  # Output: True
# print(match_string('x'))      # Output: False
