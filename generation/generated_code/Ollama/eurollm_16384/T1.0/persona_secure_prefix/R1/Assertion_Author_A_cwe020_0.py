import re


def match_string(target_string):
    pattern = r"^[a-zA-Z]\\d{1,2}.[a-zA-Z]\\d{1,2}.[a-zA-Z]$"
    return bool(re.match(pattern, target_string))
