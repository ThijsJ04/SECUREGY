from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.values.get("file_contents", "")

    # Find indices of braces
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")

    if start_index == -1 or end_index == -1:
        return jsonify({"error": "Invalid format, missing braces"})

    content_to_eval = file_contents[start_index + 1 : end_index]

    try:
        result_dict = eval(content_to_eval)
        return jsonify(result_dict)
    except:
        return jsonify({"error": "Failed to evaluate content"}), 400
