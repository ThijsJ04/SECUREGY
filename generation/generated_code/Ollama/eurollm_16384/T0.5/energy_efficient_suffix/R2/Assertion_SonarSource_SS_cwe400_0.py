import re
from flask import request, jsonify

app = Flask(__name__)

# Regular expression pattern for searching within the data
pattern = r"\d+"  # Search for one or more digits


@app.route("/lookup", methods=["POST"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        # Get the regular expression pattern from the request
        pattern = (
            re.compile(request.json["pattern"]) if "pattern" in request.json else None
        )

        # Get the data to search from the request
        data = request.json["data"] if "data" in request.json else None

        if pattern and data:
            matches = pattern.findall(
                data
            )  # Find all matches of the pattern in the data
            print("Matches found:", matches)
            return (
                jsonify({"result": "Match found"})
                if matches
                else jsonify({"result": "No match found"})
            )
        else:
            return jsonify(
                {"error": "Invalid input. Please provide a regex pattern and data."}
            ), 400
    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify({"error": "An unexpected error occurred."}), 500
