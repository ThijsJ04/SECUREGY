from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    # Extract regex and data from the request JSON
    data = request.get_json()
    if not data:
        return "No data received", 400

    pattern = data.get("regex")
    string = data.get("data")

    if not pattern or not string:
        return "Missing parameters", 400

    try:
        # Compile the regex pattern
        compiled_pattern = re.compile(pattern)
        # Search for the pattern in the string
        match = compiled_pattern.search(string)

        if match:
            return "Match found", 200
        else:
            return "No match found", 200
    except re.error:
        return "Invalid regular expression", 400


if __name__ == "__main__":
    app.run(debug=True)
