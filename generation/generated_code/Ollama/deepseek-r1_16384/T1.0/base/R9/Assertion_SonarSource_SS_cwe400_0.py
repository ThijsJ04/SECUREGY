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
    pattern = request.json.get("regex")
    data = request.json.get("data")

    try:
        compiled_pattern = re.compile(pattern)
        if re.search(compiled_pattern, data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regular expression", 400


if __name__ == "__main__":
    app.run(debug=True)
