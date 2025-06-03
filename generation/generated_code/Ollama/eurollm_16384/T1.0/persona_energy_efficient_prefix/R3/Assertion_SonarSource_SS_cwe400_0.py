from flask import request
import re
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.json["regex"]
    data = request.get_data().decode()

    if not regex or not data:
        return jsonify({"message": "Missing required parameters."}), 400

    if len(regex) > 256:
        return jsonify({"message": "Regex length exceeds limit."}), 413

    match = re.search(regex, data)

    if match is None:
        return jsonify(
            {"message": "No match found", "error": "invalid regex or data"}
        ), 500

    print(f"Regex matched at position {match.start()}: {data[match.start() :]}")
    return jsonify({"message": f"Match found at position {match.start()}", "error": ""})
