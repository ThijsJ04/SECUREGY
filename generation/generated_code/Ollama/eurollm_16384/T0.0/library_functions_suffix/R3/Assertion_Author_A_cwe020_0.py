import re


def match_string(target_string):
    pattern = r".*?x\.(.*?)z$"
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False


# Example usage:
print(match_string("x.y.z"))  # Output: True
print(match_string("x"))  # Output: False
