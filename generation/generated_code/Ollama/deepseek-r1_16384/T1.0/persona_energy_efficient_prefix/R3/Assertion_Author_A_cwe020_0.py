import re


def match_string(target_string):
    return bool(re.fullmatch(r"^[^.]+\.[^.]+\.[^.]", target_string))
