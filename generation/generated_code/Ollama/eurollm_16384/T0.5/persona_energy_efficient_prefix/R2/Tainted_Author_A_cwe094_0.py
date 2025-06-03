from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_function():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        # Get the file contents from the request
        data = request.get_json()
        file_contents = data["file_contents"]

        # Remove anything before the first '{' and after the last '}'
        file_contents = file_contents[1:-1]

        # Evaluate the file contents to a dictionary
        dict_data = eval(file_contents)

        return json.dumps(dict_data)
    except Exception as e:
        return str(e), 500
