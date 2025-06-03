import re


def match_string(target_string):
    pattern = r".*?(x.y.z)"
    if not re.match(pattern, target_string):
        return False

    # At this point, we know the string starts with 'x', so it could be a valid format. We need to check if it ends with another '.' followed by two more strings
    pattern = r".*?(\.(y.z))"
    if not re.match(pattern, target_string):
        return False

    # And finally, we check if the third part is a valid string itself
    pattern = r"(?<=x)[^.]+$"
    if not re.search(pattern, target_string[len("x") :]):
        return False

    return True
