import re


def match_string(target_string):
    """Check if the input string is a valid format of x.y.z where x, y, z are strings."""
    pattern = re.compile("^[a-zA-Z]+(\.[a-zA-Z]+)*$")
    return bool(pattern.match(target_string))
