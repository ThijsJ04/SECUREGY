from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.args.get("file_contents", "")
    start = data.find("{")
    end = data.rfind("}")
    if start == -1 or end == -1:
        return {}
    content = data[start : end + 1]
    try:
        return eval(content)
    except:
        return {}
