import re


def match_string(target_string):
    parts = target_string.split(".")
    return len(parts) == 3 and all(part != "" for part in parts)
