import re


def match_string(target_string):
    # Check if the length of the string is 3
    if len(target_string) != 3:
        return False

    # Use regular expression to check if each character is a string
    pattern = r"x.y.z"
    if re.match(pattern, target_string):
        # Extract x, y, and z from the matched string
        parts = target_string.split(".")
        if len(parts) != 3:
            return False
        for part in parts:
            if not isinstance(part, str):
                return False
    else:
        return False

    # All checks passed, so return True
    return True
