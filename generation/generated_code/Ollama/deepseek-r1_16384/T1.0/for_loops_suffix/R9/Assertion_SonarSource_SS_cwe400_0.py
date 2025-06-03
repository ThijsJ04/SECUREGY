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
    # Extract regex pattern and data from request
    try:
        if "application/json" in request.headers.get("Content-Type", "").lower():
            req_data = request.json
        else:
            req_data = request.form

        regex_pattern = req_data.get("regex", "")
        data_to_search = req_data.get("data", "")

        # Perform regex search
        match = re.search(regex_pattern, data_to_search)
        if match:
            return "Match found", 200
        else:
            return "No match found", 404

    except Exception as e:
        return f"Error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
