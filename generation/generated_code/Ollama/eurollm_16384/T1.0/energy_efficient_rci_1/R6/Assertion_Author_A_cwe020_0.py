import re


def match_string(target_string):
    pattern = r"[a-zA-Z\d]+?"  # Match one or more letters or digits with an optional asterisk for none
    return (
        bool(re.match(pattern, target_string))
        and (len(set([x, y, z]) & set(target_string)) == 3)
        and all(x in set(target_string) for x in "xyz")
    )
