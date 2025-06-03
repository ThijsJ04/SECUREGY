from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.headers.get("file_contents", None)
    if data is not None:
        start = data.find("{") if "{" in data else 0
        end = len(data) - data[-1:-1].find("}") if "}" in data[-1:] else len(data)
        content = data[start:end]
        try:
            return {content}
        except SyntaxError:
            return {"Error": "Invalid JSON format"}
