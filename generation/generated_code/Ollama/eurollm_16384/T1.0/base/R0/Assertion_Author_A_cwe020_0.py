import re


def match_string(target_string):
    pattern = r".+?\.([a-zA-Z]+)(\.[a-zA-Z]+(?:[0-9]*)?)?"
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False
