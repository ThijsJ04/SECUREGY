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
    try:
        regex = request.args.get("regex", default=None)
        data = request.args.get("data", default=None)

        if regex is None or data is None:
            return "Missing parameters"

        if re.search(regex, data):
            return "Match found"
        else:
            return "No match found"
    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
