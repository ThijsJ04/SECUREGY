from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start != -1 and end != -1:
        cleaned = file_contents[start + 1 : end]
        try:
            data = ast.literal_eval(cleaned)
            return f"data: {data}".encode()
        except Exception as e:
            return str(e).encode()
    else:
        return "Invalid format".encode()
