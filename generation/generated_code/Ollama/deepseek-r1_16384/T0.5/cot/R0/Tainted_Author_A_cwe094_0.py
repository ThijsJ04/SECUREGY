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
    content = request.args.get("file_contents", "")
    if not content:
        return jsonify({"error": "No content provided"}), 400

    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid content format"}), 400

    cleaned_content = content[start : end + 1]

    try:
        data_dict = ast.literal_eval(cleaned_content)
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
