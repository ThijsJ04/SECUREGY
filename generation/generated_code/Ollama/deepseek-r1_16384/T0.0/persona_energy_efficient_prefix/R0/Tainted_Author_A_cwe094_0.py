from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return {}
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1 or start >= end:
        return {}
    content = file_contents[start + 1 : end]
    try:
        result = ast.literal_eval(content)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except:
        return {}


if __name__ == "__main__":
    app.run(debug=True)
