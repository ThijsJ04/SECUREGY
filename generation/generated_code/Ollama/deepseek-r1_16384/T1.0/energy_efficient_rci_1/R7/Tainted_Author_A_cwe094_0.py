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
    file_content = request.args.get("file_contents") or request.form.get(
        "file_contents"
    )
    if not file_content:
        return jsonify({"error": "No content provided"})

    s = file_content.strip()
    start = s.find("{")
    end = s.rfind("}")

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format"})

    cleaned = s[start + 1 : end]
    try:
        data_dict = ast.literal_eval(cleaned)
        return jsonify(data_dict)
    except ValueError as e:
        return jsonify({"error": str(e)})
