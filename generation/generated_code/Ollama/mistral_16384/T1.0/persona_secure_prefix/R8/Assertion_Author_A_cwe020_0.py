import re


def match_string(target_string):
    return re.match(r"\b[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+){2}\b", target_string) is not None
