import re


def match_string(target_string):
    pattern = r".*?(\w+).*?(\w+).*?(\w+)"
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False
