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
    # Extract file_contents parameter from request
    file_contents = request.args.get("file_contents", "")

    # Find first and last occurrence of curly braces
    start = file_contents.find("{")
    end = file_contents.rfind("}")

    if start == -1 or end == -1:
        return json.dumps({"error": "Invalid format"})

    # Extract content between braces and evaluate as dictionary
    content_str = file_contents[start : end + 1]
    try:
        result = eval(content_str)
        return json.dumps(result)
    except SyntaxError:
        return json.dumps({"error": "Invalid syntax"})


if __name__ == "__main__":
    app.run(debug=True)
