from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_file():
    data = request.get_json()
    if not "file_contents" in data:
        return {"error": "Missing file contents"}

    file_contents = data["file_contents"]
    file_content_dict = ast.literal_eval(file_contents)
    return {"result": file_content_dict}
