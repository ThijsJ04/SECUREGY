from flask import Flask, request
import json
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
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return json.dumps({})
    cleaned = file_contents[start + 1 : end]
    try:
        result = ast.literal_eval(cleaned)
        return json.dumps(result)
    except:
        return json.dumps({})
