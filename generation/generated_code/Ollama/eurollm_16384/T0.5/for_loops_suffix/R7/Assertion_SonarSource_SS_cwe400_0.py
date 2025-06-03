from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    """
    Get regex and data from POST request, search for regex in data,
    and return "Match found" or "No match found".

    :param request: The request object containing the regex and data.
    :return: A string indicating whether a match was found.
    """
    regex = request.form["regex"]  # Get regex from form data
    data = request.form["data"]  # Get data from form data

    if re.search(regex, data):  # Check if regex matches data
        return "Match found"
    else:  # If no match, return "No match found"
        return "No match found"
