from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def evaluate_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Evaluate it to a dictionary and return its contents.
    """
    try:
        # Remove leading/trailing whitespace
        content = file_contents.strip()

        # Check if input is a valid JSON string
        if not content or not content.startswith("{") or content.endswith("}"):
            return "Error: Invalid JSON input"

        # Parse the input as JSON
        parsed_data = json.loads(content)

        # Get the content from the dictionary
        data_contents = []
        for k, v in parsed_data.items():
            data_contents.append(v)

        return "Content: {" + ", ".join([str(x) for x in data_contents]) + "}"

    except ValueError as e:
        return str(e)
