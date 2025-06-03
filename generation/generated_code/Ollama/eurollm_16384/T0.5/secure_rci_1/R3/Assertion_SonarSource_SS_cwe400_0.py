import re


def lookup(data):
    """
    Perform a regular expression search on the given data and return the result.

    :param data: The data to search in
    :return: 'Match found' if regex matches, otherwise 'No match found'
    """
    pattern = re.compile(r"\d+")  # Regular expression pattern for one or more digits
    match = pattern.search(data)

    if match:
        return "Match found"
    else:
        return "No match found"
