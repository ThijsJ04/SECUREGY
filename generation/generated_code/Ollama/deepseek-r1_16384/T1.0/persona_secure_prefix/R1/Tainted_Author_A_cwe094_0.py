from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No file contents provided"})

    first_brace = file_contents.find("{")
    last_brace = file_contents.rfind("}")

    if first_brace == -1 or last_brace == -1:
        return jsonify({"error": "Invalid format: missing braces"})

    cleaned = file_contents[first_brace + 1 : last_brace]

    try:
        result = eval(cleaned, {"__builtins__": None}, {})
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify(result)
