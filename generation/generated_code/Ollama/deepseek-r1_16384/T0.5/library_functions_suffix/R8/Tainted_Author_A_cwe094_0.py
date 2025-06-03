from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    s = request.form.get("file_contents")
    start = s.find("{")
    end = s.rfind("}")
    content = s[start : end + 1]
    return eval(content)
