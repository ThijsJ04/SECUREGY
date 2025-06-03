from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def eval_file():
    content = (
        request.get_json()
    )  # assume JSON format for 'file_contents' key in the request data
    if not content:
        return jsonify({"error": "Invalid JSON format"}), 400

    clean_content = ""
    for char in str(content):
        if char == "{":
            clean_content += char
            break
        elif char == "}":
            clean_content += char
            break
        clean_content += char

    # At this point, 'clean_content' should be a clean JSON string
    try:
        result = json.loads(
            clean_content
        )  # evaluate the clean content to get its dictionary representation
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200
