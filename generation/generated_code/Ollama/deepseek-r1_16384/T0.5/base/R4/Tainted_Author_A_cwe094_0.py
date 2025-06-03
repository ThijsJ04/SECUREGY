from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        file_contents = request.args.get("file_contents", "")
        if not file_contents:
            return jsonify({"error": "No file_contents provided"}), 400

        # Extract the part between first '{' and last '}'
        start = file_contents.find("{")
        end = file_contents.rfind("}")
        if start == -1 or end == -1:
            return jsonify({"error": "Invalid format, missing braces"}), 400
        content_to_eval = file_contents[start + 1 : end]

        # Evaluate the content as a dictionary
        try:
            data_dict = ast.literal_eval(content_to_eval)
            if not isinstance(data_dict, dict):
                raise ValueError("Content is not a dictionary")
            return jsonify(data_dict), 200
        except (ValueError, SyntaxError) as e:
            return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500
