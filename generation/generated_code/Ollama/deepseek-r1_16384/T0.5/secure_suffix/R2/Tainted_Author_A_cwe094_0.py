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
    file_contents = request.args.get("file_contents", "")
    # Extract content between first { and last }
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format"}), 400
    content = file_contents[start + 1 : end].strip()
    # Safely evaluate the string to a dictionary
    try:
        request_data = ast.literal_eval(content)
        return jsonify(request_data)
    except (ValueError, SyntaxError):
        return jsonify({"error": "Invalid JSON"}), 400
