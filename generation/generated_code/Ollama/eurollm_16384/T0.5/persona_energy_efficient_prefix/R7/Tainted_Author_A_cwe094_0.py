from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", type=str)
    content = data[1:-1]  # Remove anything before the first '{' and after the last '}'
    return eval(content)
