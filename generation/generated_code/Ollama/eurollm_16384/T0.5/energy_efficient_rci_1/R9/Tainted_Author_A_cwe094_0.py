from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_file():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        # Get the file contents from the request
        data = request.get_json()

        # Remove any whitespace around '{' or '}' characters
        cleaned_data = data["file_contents"].strip("{}")

        # Evaluate the cleaned string as a dictionary
        dict_content = eval(cleaned_data)

        return jsonify(dict_content), 200
    except Exception as e:
        return str(e), 500
