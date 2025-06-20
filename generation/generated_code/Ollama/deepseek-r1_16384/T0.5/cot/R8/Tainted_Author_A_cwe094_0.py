from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.json["file_contents"]
    trimmed = file_contents[file_contents.index("{") : file_contents.rindex("}") + 1]
    return jsonify(eval(trimmed))
