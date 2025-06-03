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
        # Get data from request
        if request.is_json:
            data = request.json
        else:
            data = request.values

        # Extract regex and text from request
        regex_pattern = data.get("regex", None)
        input_text = data.get("data", None)

        if not regex_pattern or not input_text:
            return {"error": "Missing required parameter"}, 400

        # Perform regex search
        if re.search(regex_pattern, input_text):
            return {"result": "Match found"}
        else:
            return {"result": "No match found"}

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run()
