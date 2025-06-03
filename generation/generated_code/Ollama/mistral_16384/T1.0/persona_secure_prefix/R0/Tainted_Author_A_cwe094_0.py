from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")

    if not file_contents:
        return jsonify({"error": "No file contents provided."}), 400

    # Remove any characters before the first '{' and after the last '}'
    cleaned_content = file_contents[file_contents.find("{") :].strip()

    try:
        content_dict = ast.literal_eval(cleaned_content)
        return jsonify(content_dict)
    except (SyntaxError, ValueError):
        return jsonify({"error": "Invalid JSON or dictionary format."}), 400
