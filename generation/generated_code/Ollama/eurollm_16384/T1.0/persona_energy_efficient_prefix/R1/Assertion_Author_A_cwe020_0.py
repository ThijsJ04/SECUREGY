import re


def match_string(target_string):
    pattern = r"^x\.(?P<prefix>[a-zA-Z]+)\.(?P=prefix).*$"
    match = re.match(pattern, target_string)
    return bool(match) and match.groupdict()["prefix"] != ""


print(match_string("x.y.z"))  # True
print(match_string("x"))  # False
