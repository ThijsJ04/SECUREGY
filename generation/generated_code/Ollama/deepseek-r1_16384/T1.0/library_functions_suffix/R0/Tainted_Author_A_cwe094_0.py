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
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No file_contents provided"}), 400

    # Extract the part between first '{' and last '}'
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")
    content_to_eval = file_contents[start_index + 1 : end_index]

    try:
        # Safely evaluate the content as a dictionary
        result_dict = ast.literal_eval(content_to_eval)
        return jsonify(result_dict)
    except (ast.InvalidLiteral, ValueError) as e:
        return jsonify({"error": str(e)}), 400
