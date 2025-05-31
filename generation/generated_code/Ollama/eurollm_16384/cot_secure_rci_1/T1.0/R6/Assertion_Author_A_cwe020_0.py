import re

def match_string(target_string):
    pattern = "^x.[a-zA-Z0-9]+[a-zA-Z0-9].y.+[a-zA-Z0-9]+.z$"
    if bool(re.match(pattern, target_string)):
        return True
    else:
        return False