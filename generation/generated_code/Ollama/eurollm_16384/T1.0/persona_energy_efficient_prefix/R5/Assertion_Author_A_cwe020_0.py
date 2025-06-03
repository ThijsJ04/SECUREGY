import re


def match_string(target_string):
    # Define the pattern for a valid string format (x.y.z)
    pattern = r"^[a-zA-Z0-9]+(.[a-zA-Z0-9]+)+$"

    # Use re.match to check if the target_string matches the pattern
    if re.match(pattern, target_string):
        return True
    else:
        return False


# Example usage
print(match_string("x.y.z"))  # Output: True
print(match_string("x"))  # Output: False
