from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No file_contents provided"}), 400

    start = file_contents.find("{")
    end = file_contents.rfind("}")

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format, missing braces"}), 400

    content = file_contents[start : end + 1]

    try:
        # Using ast.literal_eval for safer evaluation
        result = ast.literal_eval(content)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
