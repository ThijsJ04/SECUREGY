import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_input = request.args.get("regex")
    data_input = request.args.get("data")

    # Remove leading and trailing whitespace from regex input
    regex_input = re.escape(regex_input).strip()

    if not regex_input or not data_input:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        pattern = re.compile(regex_input)
        matches = pattern.finditer(data_input)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if not matches:
        return jsonify({"result": "No match found"}), 200
    else:
        search_results = [match.group() for match in matches]
        return jsonify({"result": "Match found", "matches": search_results})
