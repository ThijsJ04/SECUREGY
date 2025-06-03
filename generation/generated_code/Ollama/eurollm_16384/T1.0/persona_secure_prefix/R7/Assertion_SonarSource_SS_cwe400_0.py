from flask import request, jsonify
import re

app = Flask(__name__)

# Replace with your desired regex pattern
regex_pattern = r"\d+"  # Example: matches one or more digits


@app.route("/lookup", methods=["GET"])
def lookup():
    data = request.args.get("data")
    if not data:
        return jsonify({"result": "Data is empty"})

    match = re.search(regex_pattern, str(data))
    if match:
        return jsonify({"result": "Match found", "matched_value": match.group()})
    else:
        return jsonify({"result": "No match found"})
