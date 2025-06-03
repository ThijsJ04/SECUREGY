from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.args.get("file_contents", "")
    if not data:
        return {}
    start = data.find("{")
    end = data.rfind("}")
    if start == -1 or end == -1 or start > end:
        return {}
    cleaned = data[start : end + 1]
    try:
        result = ast.literal_eval(cleaned)
        return result if isinstance(result, dict) else {}
    except (ValueError, SyntaxError):
        return {}


if __name__ == "__main__":
    app.run(debug=True)
