from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.get_json()  # Assuming JSON data is sent in the request body
    file_contents = data["file_contents"]

    # Remove anything before the first '{' and after the last '}'
    file_contents = file_contents[1:-1]

    try:
        result = eval(file_contents)  # Evaluate the content as a Python expression
        return json.dumps(result)
    except Exception as e:
        return str(e), 500
