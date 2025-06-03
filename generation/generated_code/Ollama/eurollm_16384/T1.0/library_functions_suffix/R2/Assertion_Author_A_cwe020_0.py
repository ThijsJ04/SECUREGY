import re


def match_string(target_string):
    pattern = r"[a-zA-Z\s]+?([0-9]\.)?"
    if not re.match(pattern, target_string):
        return False
    matches = re.findall(r"(.*?)", target_string)
    for m in matches:
        if len(m) != 3 or any(not isinstance(c, str) for c in m):
            return False
    return True
