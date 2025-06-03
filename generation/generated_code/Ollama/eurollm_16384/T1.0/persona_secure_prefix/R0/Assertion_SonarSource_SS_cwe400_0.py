import re
from flask import request, jsonify
from flask import Flask

app = Flask(__name__)


def lookup(regex):
    """
    Get regex from request and search for it in data.
    Returns "Match found" if the pattern is matched, otherwise "No match found".

    :param regex: Regular expression to search for
    :return: search result
    """
    try:
        # Convert the string into a regular expression object
        compiled_regex = re.compile(regex)

        # Read the data from the request body and convert it to a list of strings
        data = [line.strip() for line in request.data.decode().split("\n")]

        # Iterate over each string in the data, apply the compiled regex, and return the result
        for d in data:
            if compiled_regex.search(d):
                return "Match found"
        return "No match found"
    except Exception as e:
        return str(e)
