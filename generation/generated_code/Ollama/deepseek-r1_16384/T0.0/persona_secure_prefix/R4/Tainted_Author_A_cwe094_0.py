from flask import Flask, request
import ast  # Added for safe evaluation

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
        return "Bad request", 400

    start = file_contents.find("{")
    end = file_contents.rfind("}")

    if start == -1 or end == -1:
        return "Invalid format", 400

    content = file_contents[start : end + 1]

    try:
        # Using ast.literal_eval for safer evaluation
        result = ast.literal_eval(content)
        return app.jsonify(result)
    except Exception as e:
        return f"Error parsing content: {str(e)}", 500
