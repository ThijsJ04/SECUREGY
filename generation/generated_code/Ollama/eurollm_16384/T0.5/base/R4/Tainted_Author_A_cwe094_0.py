from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def eval_request():
    """
    Evaluate the given JSON string as Python code.
    """
    data = request.args.get("file_contents")
    if not data:
        return "No file contents provided."

    try:
        tree = ast.parse(data)
        result = eval(compile(tree, filename="<string>", mode="eval"))
        return str(result)
    except Exception as e:
        return f"Error evaluating code: {e}"
