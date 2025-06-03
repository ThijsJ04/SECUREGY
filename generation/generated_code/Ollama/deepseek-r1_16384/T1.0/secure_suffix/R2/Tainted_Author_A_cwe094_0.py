from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.form.get("file_contents", "")
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        return jsonify({})

    processed = content[start + 1 : end]

    try:
        data_dict = json.loads(processed)
    except json.JSONDecodeError as e:
        app.logger.error(f"Invalid JSON: {e}")
        return jsonify({"error": "The provided content is not a valid dictionary."})

    if not isinstance(data_dict, dict):
        return jsonify({"error": "Content could not be parsed into a dictionary"})

    return jsonify(data_dict)
