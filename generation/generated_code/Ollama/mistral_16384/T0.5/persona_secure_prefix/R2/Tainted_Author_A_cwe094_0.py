from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", type=str)

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = file_contents[file_contents.find("{") :].strip()

    try:
        return jsonify(ast.literal_eval(cleaned_content))
    except (SyntaxError, ValueError):
        return "Invalid JSON", 400
