from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents") or request.form.get(
        "file_contents"
    )
    if not file_contents:
        return jsonify({"error": "No file_contents provided"}), 400

    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid content format"}), 400

    content = file_contents[start : end + 1]
    try:
        result = eval(content)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
