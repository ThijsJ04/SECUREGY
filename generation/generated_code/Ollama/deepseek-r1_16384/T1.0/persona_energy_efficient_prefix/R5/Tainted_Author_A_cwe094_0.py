from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the file_contents parameter from the request
    content_str = request.args.get("file_contents", "")

    if not content_str:
        return jsonify({"error": "No file_contents provided"}), 400

    try:
        # Remove everything before first '{' and after last '}'
        cleaned = content_str.split("{", 1)[1].rsplit("}", 1)[0]

        # Evaluate the string to a dictionary
        data_dict = json.loads(cleaned)
        return jsonify(data_dict), 200

    except (IndexError, json.JSONDecodeError) as e:
        return jsonify({"error": str(e)}), 400
