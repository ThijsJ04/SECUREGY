from flask import Flask, request
from flask import jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_content_str = request.args.get("file_contents")

    if not file_content_str:
        return jsonify({"error": "No file_contents provided"})

    start = file_content_str.find("{")
    end = file_content_str.rfind("}")

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid content format"})

    content_to_evaluate = file_content_str[start + 1 : end]

    try:
        result_dict = eval(content_to_evaluate)
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify(result_dict)
