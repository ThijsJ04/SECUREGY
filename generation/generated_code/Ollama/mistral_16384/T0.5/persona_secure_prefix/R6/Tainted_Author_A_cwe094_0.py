from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return jsonify({"error": "No 'file_contents' provided."}), 400

    # Remove anything before the first '{' and after the last '}'
    start = file_contents.find("{")
    end = file_contents.rfind("}") + 1
    content = file_contents[start:end]

    # Evaluate it to a dictionary
    return jsonify(ast.literal_eval(content))
