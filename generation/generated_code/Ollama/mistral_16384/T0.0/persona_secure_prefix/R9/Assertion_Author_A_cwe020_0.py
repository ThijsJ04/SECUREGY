import re


def match_string(target_string):
    pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$"
    if re.match(pattern, target_string):
        return True
    else:
        return False


# Original code remains unchanged
