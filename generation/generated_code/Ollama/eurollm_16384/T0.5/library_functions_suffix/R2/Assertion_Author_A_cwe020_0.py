import re


def match_string(target_string):
    pattern = r".*?[xyz](\d+).*?"
    match = re.search(pattern, target_string)
    return bool(match) and len(match.groups()) == 2
