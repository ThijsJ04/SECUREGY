from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_post():
    """
    Evaluates the content in the request body as a Python expression and returns its result.
    """
    data = request.get_json()
    if not "file_contents" in data:
        return {"error": "Missing file contents"}, 400

    content = data["file_contents"]
    # Remove anything before the first '{' and after the last '}'
    content = content[content.find("{") + 1 : content.rfind("}")]

    result = eval(content)  # Evaluate the content as a Python expression

    return {"result": result}, 200
