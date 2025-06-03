from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_json():
    data = request.get_json()
    file_contents = data.get("file_contents")
    if file_contents is None:
        return "No file contents provided", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = file_contents[
        1:-1
    ]  # Assuming '{' is at index 1 and '}' at index -1

    # Evaluate the cleaned content to a dictionary
    try:
        result_dict = eval(cleaned_content)
    except Exception as e:
        return str(e), 500  # Return an error if evaluation fails

    return json.dumps(result_dict, indent=4), 201
