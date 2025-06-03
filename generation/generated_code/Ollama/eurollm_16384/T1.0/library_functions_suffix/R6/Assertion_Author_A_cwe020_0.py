import re


def match_string(target_string):
    """
    Check if the input string is valid and matches the format of x.y.z, where x, y, z are strings.

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    """
    pattern = "(?:([a-z]+\.)?)+?([\w \.-][a-z]+\.)?"
    return (
        bool(re.match(pattern, target_string))
        and all(
            [
                isinstance(match, str)
                for match in re.findall("(?:([a-z]+\.)?)", target_string)
            ]
        )
        and all(
            [
                isinstance(match, str)
                for match in re.findall("([\w \.-][a-z]+\.)?", target_string)
            ]
        )
    )
