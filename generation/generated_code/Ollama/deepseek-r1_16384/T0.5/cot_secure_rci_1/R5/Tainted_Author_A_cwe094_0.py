from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.form.get("file_contents")
    if not file_contents:
        return jsonify({"error": "No content provided"}), 400

    first_brace = file_contents.find("{") + 1
    last_brace = file_contents.rfind("}")

    content_to_eval = file_contents[first_brace:last_brace]
    data_dict = eval(content_to_eval)

    return jsonify(data_dict)
