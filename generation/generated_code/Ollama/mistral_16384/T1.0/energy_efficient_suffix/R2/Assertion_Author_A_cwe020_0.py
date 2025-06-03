import re


def match_string(target_string):
    return bool(re.match(r"[a-zA-Z\.]+\.[a-zA-Z\.]+\.[a-zA-Z\.]+", target_string))
