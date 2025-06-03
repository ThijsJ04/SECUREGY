from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    """
    Evaluate the contents of a file and return its value.
    """
    data = request.data

    # Remove any leading or trailing whitespace
    data = data.strip()

    # Evaluate the contents as a Python expression
    try:
        content_dict = eval(data)
        return content_dict, 200
    except Exception as e:
        return str(e), 500
