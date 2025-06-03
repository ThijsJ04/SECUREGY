from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_json():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON format"}), 400

    # Evaluate the JSON to a dictionary and return its contents
    contents = eval(json.dumps(data)) if data else None

    if not isinstance(contents, dict):
        return jsonify({"error": "Invalid JSON content"}), 400

    return jsonify(contents)
