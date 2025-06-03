import json
from flask import request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    file_contents = request.form[
        "file_contents"
    ]  # Assuming the JSON string is in a form field named 'file_contents'
    try:
        data = json.loads(
            file_contents
        )  # Load the JSON string into a Python dictionary
        return str(
            data
        )  # Convert the dictionary to a string and return it as the response
    except ValueError:
        return "Invalid JSON format"
