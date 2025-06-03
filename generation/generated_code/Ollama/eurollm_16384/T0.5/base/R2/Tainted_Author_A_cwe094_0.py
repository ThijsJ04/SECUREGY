from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    file_contents = request.form[
        "file_contents"
    ]  # Get the file contents from the form data
    content = file_contents[
        1:-1
    ]  # Remove any text before the first '{' and after the last '}'
    try:
        dict_content = json.loads(content)  # Try to parse the content into a dictionary
        return json.dumps(dict_content)  # Return the dictionary as JSON
    except ValueError:
        return (
            "Invalid JSON",
            400,
        )  # If the content is not valid JSON, return an error response
