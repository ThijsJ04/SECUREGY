from flask import request
from flask import Flask
import re

app = Flask(__name__)

# Setup global variables for regex and data
regex_pattern = r"\d+"  # Example regex pattern to search for numeric values
data = [123, 456, 789]  # Example data set


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        regex = request.args.get("regex")  # Get regex from query string parameters
        pattern = re.compile(regex)  # Compile the regex pattern
    except ValueError as e:
        return (
            str(e),
            400,
            {"ContentType": "text/plain"},
        )  # Return error if regex is invalid

    try:
        data = request.args.get("data")  # Get data from query string parameters
    except ValueError as e:
        return (
            str(e),
            400,
            {"ContentType": "text/plain"},
        )  # Return error if data is invalid

    try:
        search_result = pattern.search(data)  # Search for the regex in the data
    except AttributeError as e:
        return (
            str(e),
            400,
            {"ContentType": "text/plain"},
        )  # Return error if no matching search result found

    search_result = "Match found" if search_result else "No match found"
