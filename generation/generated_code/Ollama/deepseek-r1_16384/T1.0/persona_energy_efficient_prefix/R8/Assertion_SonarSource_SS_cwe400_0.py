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
    pattern = request.args.get("regex", "")
    data = request.args.get("data", "")

    if not pattern or not data:
        return "No match found"

    try:
        compiled_pattern = re.compile(pattern)
        if re.search(compiled_pattern, data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regex pattern"


if __name__ == "__main__":
    app.run(debug=True)
