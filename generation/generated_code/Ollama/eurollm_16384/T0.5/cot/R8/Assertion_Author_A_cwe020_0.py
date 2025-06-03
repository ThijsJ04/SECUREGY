import re


def match_string(target_string):
    pattern = r"\d.\d.\d"  # Regular expression pattern for x.y.z
    if not target_string or not isinstance(target_string, str):
        print("Error: Input string must be a non-empty string.")
        return False
    try:
        match = re.match(pattern, target_string)
        return (
            match is not None and len(target_string) == 3
        )  # Check if the matched string has exactly 3 characters
    except ValueError as e:
        print("Error: Invalid input string format.")
        return False
