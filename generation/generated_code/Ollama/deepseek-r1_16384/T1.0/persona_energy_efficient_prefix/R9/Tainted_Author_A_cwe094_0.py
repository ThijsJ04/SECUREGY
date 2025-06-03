from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    # Get data from the request using 'file_contents'
    content = None
    if request.is_json:
        content = request.json.get("file_contents", "")
    else:
        content = request.values.get("file_contents", "")

    if not content:
        return jsonify({"error": "No file_contents provided"})

    # Remove anything before the first '{' and after the last '}'
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format: missing braces"})

    content_str = content[start : end + 1].strip()

    # Evaluate the string to a dictionary
    try:
        result_dict = json.loads(content_str)
        if not isinstance(result_dict, dict):
            raise ValueError("Result is not a dictionary.")
        return jsonify(result_dict)
    except Exception as e:
        app.logger.error(f"Error parsing content: {e}")
        return jsonify({"error": str(e)}), 400
