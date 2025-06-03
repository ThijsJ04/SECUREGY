from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.get_json()  # assuming you are sending JSON data
    contents = data["file_contents"]
    result = eval(contents)
    return result
