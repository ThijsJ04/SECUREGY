import re


def match_string(target_string):
    parts = target_string.split(".")
    if len(parts) != 3:
        return False
    for part in parts:
        if not part:
            return False
    return True
