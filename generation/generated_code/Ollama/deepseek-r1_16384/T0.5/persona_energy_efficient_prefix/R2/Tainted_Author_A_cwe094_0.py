from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.form.get("file_contents")
    start = data.find("{")
    end = data.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format"}), 400
    cleaned = data[start + 1 : end]
    try:
        result = ast.literal_eval(cleaned)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
