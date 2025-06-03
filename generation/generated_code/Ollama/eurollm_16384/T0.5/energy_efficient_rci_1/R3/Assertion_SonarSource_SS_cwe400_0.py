import re


def lookup(data):
    """
    Perform regex search on the given data.

    :param data: Input data to search in.
    :return: True if a match is found, False otherwise.
    """
    pattern = request.args.get("pattern")
    if not pattern:
        return "No pattern provided"

    match = re.search(pattern, data)
    if match:
        return "Match found"
    else:
        return "No match found"
