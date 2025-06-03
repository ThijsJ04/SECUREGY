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
    pattern = request.form.get("pattern")
    data = request.form.get("data")
    if not pattern or not data:
        return "Invalid input"
    try:
        compiled_pattern = re.compile(pattern)
        match = compiled_pattern.search(data)
        return "Match found" if match else "No match found"
    except re.error:
        return "Invalid regex pattern"


if __name__ == "__main__":
    app.run(debug=True)
