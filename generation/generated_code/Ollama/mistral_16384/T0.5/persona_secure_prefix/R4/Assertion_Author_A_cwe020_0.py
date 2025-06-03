import re


def match_string(target_string):
    if not target_string or not re.match(
        r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$", target_string
    ):
        return False
    parts = target_string.split(".")
    return all([part for part in parts if part])
