import re


def match_string(target_string):
    pattern = r".+?\.(?P<x>[a-zA-Z]).+\.(?P<y>[a-zA-Z]).+$"
    match = re.search(pattern, target_string)
    if match:
        x = match.group("x")
        y = match.group("y")
        return x and y
    else:
        return False
