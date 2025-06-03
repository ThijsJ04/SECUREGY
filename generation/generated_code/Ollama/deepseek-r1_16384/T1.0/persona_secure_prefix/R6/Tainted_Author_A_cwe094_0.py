from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.values.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No file_contents provided"}), 400
    start_idx = file_contents.find("{")
    if start_idx == -1:
        return jsonify({"error": "Missing opening brace"}), 400
    end_idx = file_contents.rfind("}")
    if end_idx == -1 or end_idx < start_idx:
        return jsonify({"error": "Missing closing brace"}), 400
    content_to_eval = file_contents[start_idx : end_idx + 1]
    try:
        data_dict = ast.literal_eval(content_to_eval)
        if not isinstance(data_dict, dict):
            return jsonify({"error": "Content is not a dictionary"}), 400
        return jsonify(data_dict)
    except ValueError as e:
        app.logger.error(f"Failed to evaluate content: {e}")
        return jsonify({"error": "Invalid content"}), 500
