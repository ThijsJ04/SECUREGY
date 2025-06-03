import re


def match_string(target_string):
    pattern = (
        r"^[a-zA-Z0-9]+$"  # Match alphanumeric characters with optional leading dot
    )
    return bool(re.match(pattern, target_string)) if "." in target_string else False


print(match_string("x.y.z"))  # True
print(match_string("x"))  # False
