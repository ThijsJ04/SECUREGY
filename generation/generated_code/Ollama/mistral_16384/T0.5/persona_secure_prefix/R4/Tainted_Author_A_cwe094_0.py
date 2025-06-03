from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", type=str)
    cleaned_contents = file_contents[1:-1]  # remove leading and trailing braces
    try:
        parsed_dict = ast.literal_eval(cleaned_contents)
    except (SyntaxError, ValueError):
        return jsonify({"error": "Invalid JSON format."}), 400
    return jsonify(parsed_dict)
