import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    """Search for a pattern within data using regex."""
    data_post = request.get_json()
    if not data_post:
        return jsonify({"error": "No JSON data provided"}), 400

    regex = request.json["regex"]
    matches = []
    for item in data_post:
        pattern = r"^{0}".format(regex)  # escape the regex for safe comparison
        if re.match(pattern, str(item)) is not None:
            matches.append(
                {
                    "key": item["key"],  # replace 'key' with your actual key column
                    "value": item["value"],
                }
            )
    return jsonify(matches) if matches else {"message": "No match found"}
