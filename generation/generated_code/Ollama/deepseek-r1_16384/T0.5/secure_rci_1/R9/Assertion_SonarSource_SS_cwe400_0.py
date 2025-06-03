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
    regex_pattern = request.args.get("regex", "")
    data_to_search = request.args.get("data", "")

    try:
        pattern = re.compile(regex_pattern)
        if pattern.search(data_to_search):
            return jsonify("Match found")
        else:
            return jsonify("No match found")
    except re.error:
        return jsonify("Invalid regex pattern"), 400


if __name__ == "__main__":
    app.run(debug=True)
