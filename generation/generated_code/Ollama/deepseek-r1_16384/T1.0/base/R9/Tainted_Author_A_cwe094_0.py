from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.form.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No file contents provided"}), 400
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")
    if start_index == -1 or end_index == -1:
        return jsonify({"error": "Invalid content format"}), 400
    content_to_eval = file_contents[start_index + 1 : end_index]
    try:
        # Use ast.literal_eval for safe evaluation of literals
        result_dict = ast.literal_eval(content_to_eval)
        if not isinstance(result_dict, dict):
            return jsonify({"error": "Content is not a dictionary"}), 400
        return jsonify(result_dict)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
