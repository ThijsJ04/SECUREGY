import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_str = request.args.get("regex")
    data = request.args.get("data")

    # Ensure both regex and data are provided
    if not regex_str or not data:
        return jsonify({"error": "Missing required parameters"}), 400

    match = re.search(regex_str, data)
    if match:
        return jsonify({"result": "Match found"})
    else:
        return jsonify({"result": "No match found"})
