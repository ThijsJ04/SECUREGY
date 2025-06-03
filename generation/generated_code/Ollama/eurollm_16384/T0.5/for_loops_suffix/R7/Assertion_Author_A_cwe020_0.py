import re


def match_string(target_string):
    pattern = r".*?(\d+).*?(\d+).*?"
    match = re.search(pattern, target_string)
    if match:
        return True
    else:
        return False
