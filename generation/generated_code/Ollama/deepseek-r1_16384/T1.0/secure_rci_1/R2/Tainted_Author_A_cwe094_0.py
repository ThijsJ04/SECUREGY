from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """

    # Extract the content from the request
    if request.is_json:
        content = request.json.get("file_contents", "{}")
    else:
        content = request.values.get("file_contents", "{}")

    # Find the first and last occurrence of braces
    start_idx = content.find("{")
    end_idx = content.rfind("}")

    # If braces are not found, default to empty dict string
    if start_idx == -1 or end_idx == -1:
        processed_content = "{}"
    else:
        processed_content = content[start_idx : end_idx + 1]

    # Evaluate the processed JSON string into a dictionary
    try:
        return json.loads(processed_content)
    except json.JSONDecodeError:
        return {}
