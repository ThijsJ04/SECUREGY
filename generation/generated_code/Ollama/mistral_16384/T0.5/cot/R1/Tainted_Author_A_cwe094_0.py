from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", None)
    if data:
        start = data.find("{") + 1
        end = len(data) - data[-1::-1].index("}")
        content = data[start:end]
        return {"content": eval(content)}
