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
    if request.is_json:
        regex = request.json.get("regex")
        data = request.json.get("data")
    else:
        regex = request.args.get("regex")
        data = request.args.get("data")

    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"


if __name__ == "__main__":
    app.run(debug=True)
