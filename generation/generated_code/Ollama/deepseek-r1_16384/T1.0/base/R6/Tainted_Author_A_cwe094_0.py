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
    file_contents = request.args.get("file_contents", "")

    if not file_contents:
        return jsonify({"error": "No file contents provided"}), 400

    try:
        # Find the first occurrence of '{'
        start_index = file_contents.find("{")
        if start_index == -1:
            return jsonify({"error": "No opening brace found"}), 400

        # Slice from first '{' to end
        substring = file_contents[start_index:]

        # Find the last occurrence of '}'
        end_index = substring.rfind("}")
        if end_index == -1:
            return jsonify({"error": "No closing brace found"}), 400

        # Slice up to the last '}'
        cleaned_content = substring[:end_index]

        # Evaluate the cleaned content as a dictionary
        result_dict = eval(cleaned_content)

        return jsonify(result_dict)

    except Exception as e:
        return jsonify({"error": str(e)}), 400
