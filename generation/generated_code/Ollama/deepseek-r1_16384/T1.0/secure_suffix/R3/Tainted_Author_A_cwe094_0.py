from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.values.get("file_contents", "")
    if not data:
        return jsonify({"error": "No file_contents provided"}), 400
    start = data.find("{")
    end = data.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format: missing braces"}), 400
    content = data[start : end + 1]
    try:
        result = ast.literal_eval(content)
        if not isinstance(result, dict):
            return jsonify({"error": "Result is not a dictionary"}), 400
    except (ValueError, SyntaxError) as e:
        return jsonify({"error": f"Invalid syntax: {str(e)}"}), 400
    return jsonify(result)
