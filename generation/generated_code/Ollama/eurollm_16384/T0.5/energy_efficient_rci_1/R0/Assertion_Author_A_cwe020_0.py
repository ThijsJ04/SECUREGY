import re


def match_string(target_string):
    pattern = r".*?x\.(.*?)z$"
    if re.match(pattern, target_string):
        return True
    else:
        return False
