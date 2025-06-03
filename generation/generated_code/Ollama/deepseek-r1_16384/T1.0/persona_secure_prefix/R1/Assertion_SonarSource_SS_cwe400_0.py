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
    if "regex" not in request.args or "data" not in request.args:
        return {"error": "Missing required parameter"}, 400

    pattern = request.args["regex"]
    data = request.args["data"]

    try:
        match = re.search(pattern, data)
        if match:
            return {"result": "Match found"}, 200
        else:
            return {"result": "No match found"}, 200
    except re.error as e:
        return {"error": f"Invalid regular expression: {str(e)}"}, 400


if __name__ == "__main__":
    app.run(debug=True)
