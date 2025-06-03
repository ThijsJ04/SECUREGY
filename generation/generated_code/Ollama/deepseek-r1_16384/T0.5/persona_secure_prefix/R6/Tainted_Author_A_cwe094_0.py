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
    # Retrieve the file_contents parameter from request
    content = request.args.get("file_contents", "")

    # Extract substring between first { and last }
    start = content.find("{")
    end = content.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format, missing braces"})
    extracted = content[start + 1 : end]

    # Safely evaluate the string to a dictionary
    try:
        data_dict = ast.literal_eval(extracted)
        return jsonify(data_dict)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
