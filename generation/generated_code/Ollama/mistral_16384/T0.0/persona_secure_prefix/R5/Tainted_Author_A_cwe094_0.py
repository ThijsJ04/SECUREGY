from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)
    if not file_contents:
        return jsonify({"error": "No file_contents provided."}), 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = file_contents[file_contents.find("{") :]
    cleaned_content = cleaned_content[: cleaned_content.rfind("}") + 1]

    try:
        return jsonify(ast.literal_eval(cleaned_content))
    except Exception as e:
        return jsonify({"error": str(e)})
