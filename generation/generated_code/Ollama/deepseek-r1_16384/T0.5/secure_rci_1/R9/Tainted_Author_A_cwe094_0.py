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
    content = request.args.get("file_contents", "")
    start_idx = content.find("{")
    end_idx = content.rfind("}")

    if start_idx == -1 or end_idx == -1:
        return {}

    expr = content[start_idx : end_idx + 1]
    try:
        result = json.loads(expr)
    except json.JSONDecodeError:
        return {}
    return result
