from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.files["file_contents"]
    contents = data.read().decode("utf-8")
    start_index = contents.find("{") + 1
    end_index = contents.rfind("}")
    if start_index > end_index:
        return {}, 400
    return eval(contents[start_index:end_index]), 200
