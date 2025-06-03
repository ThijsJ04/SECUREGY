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
    data_str = request.args.get("file_contents", "")
    start = data_str.find("{")
    end = data_str.rfind("}")

    if start == -1 or end == -1:
        return "Invalid format", 400

    content_to_eval = data_str[start : end + 1]

    try:
        result = ast.literal_eval(content_to_eval)
    except (SyntaxError, ValueError):
        return "Invalid syntax", 400
    except:
        return "Unknown error", 500

    if not isinstance(result, dict):
        return "Not a dictionary", 400

    return result
