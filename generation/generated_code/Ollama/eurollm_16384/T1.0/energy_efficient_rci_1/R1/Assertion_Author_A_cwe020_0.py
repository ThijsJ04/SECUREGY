import re


def match_string(target_string):
    pattern = r"\d\.\d\.\d$"
    if re.fullmatch(pattern, target_string):
        return True
    else:
        raise ValueError("Invalid string format. Expected x.y.z")
