import re


def match_string(target_string):
    pattern = r"x.[^.]*z$"
    return bool(re.match(pattern, target_string))
