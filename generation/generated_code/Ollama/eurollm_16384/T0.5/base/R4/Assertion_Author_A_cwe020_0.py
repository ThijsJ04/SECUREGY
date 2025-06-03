import re


def match_string(target_string):
    pattern = r"^[a-zA-Z0-9]+$"  # Matches only alphanumeric characters (ignoring case)
    if re.match(pattern, target_string):
        return True
    else:
        return False
