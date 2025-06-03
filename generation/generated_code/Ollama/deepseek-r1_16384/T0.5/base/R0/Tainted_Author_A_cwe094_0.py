from flask import Flask, request
import ast
from flask.json import jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return jsonify({"error": "No content provided"}), 400
    start_idx = file_contents.find("{")
    end_idx = file_contents.rfind("}")
    if start_idx == -1 or end_idx == -1:
        return jsonify({"error": "Invalid format"}), 400
    content_to_eval = file_contents[start_idx : end_idx + 1]
    try:
        result_dict = ast.literal_eval(content_to_eval)
        return jsonify(result_dict)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
