from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content_str = request.args.get("file_contents", "")
    start = content_str.find("{")
    end = content_str.rfind("}")
    if start == -1 or end == -1:
        return {}
    content_slice = content_str[start : end + 1]
    try:
        result = ast.literal_eval(content_slice)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except:
        return {}


if __name__ == "__main__":
    app.run(debug=True)
