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
    regex_pattern = request.args.get("regex", "").strip()
    data_str = request.args.get("data", "").strip()

    try:
        safe_regex = re.escape(regex_pattern)
        match_found = bool(re.search(safe_regex, data_str))
    except re.error:
        match_found = False

    return "Match found" if match_found else "No match found"


if __name__ == "__main__":
    app.run(debug=True)
