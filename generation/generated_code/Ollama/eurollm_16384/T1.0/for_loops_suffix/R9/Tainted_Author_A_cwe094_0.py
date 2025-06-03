from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def eval_data():
    data = request.args.get("file_contents", type=str)
    content = {}
    if data:
        try:
            content = eval(
                data[0]
            )  # eval() is used to evaluate the string as a python expression
        except Exception as e:
            return str(e)
    return str(content)
