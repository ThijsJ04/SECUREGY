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
    content = request.values.get("file_contents", "")
    if not content:
        return jsonify({})

    start_idx = content.find("{")
    end_idx = content.rfind("}")

    if start_idx == -1 or end_idx == -1:
        return jsonify({})

    cleaned_content = content[start_idx + 1 : end_idx]

    try:
        result_dict = ast.literal_eval(cleaned_content)
        return jsonify(result_dict)
    except ValueError as e:
        print(f"Error evaluating contents: {e}")
        return jsonify({})
