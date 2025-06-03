import re


def match_string(target_string):
    pattern = r"(\d+).(\d+).(\d+)"  # . matches any single character, + means one or more occurrences
    match = re.match(pattern, target_string)
    return bool(
        match
        and (
            len(match.group(1)) == 1
            and len(match.group(2)) == 1
            and len(match.group(3)) == 1
        )
    )
