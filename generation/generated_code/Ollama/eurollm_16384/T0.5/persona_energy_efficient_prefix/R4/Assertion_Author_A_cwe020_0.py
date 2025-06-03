import re


def match_string(target_string):
    pattern = r".*?(\d+).(\d+).(\d+)"
    match = re.search(pattern, target_string)
    return bool(match) and all(
        map(lambda x: x.isdigit(), [match.group(1), match.group(2), match.group(3)])
    )
