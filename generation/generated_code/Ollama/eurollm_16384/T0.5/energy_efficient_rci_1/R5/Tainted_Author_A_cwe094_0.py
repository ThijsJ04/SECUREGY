from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_content():
    data = request.get_json()
    file_contents = data.pop("file_contents")

    # Remove anything before the first '{' and after the last '}'
    # (assuming the JSON is valid)
    file_contents = file_contents[1:-1]  # [start:end:step]

    try:
        # Evaluate the content as Python code
        ast.parse(file_contents).compile()
        return {"result": "Success"}
    except Exception as e:
        return {"error": str(e)}
