from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def eval_contents():
    data = request.args.get("file_contents", default=None)
    if not data:
        return "No file contents provided"

    content = data.strip()
    result = eval(content[1:-1])  # Remove the first '{' and last '}'
    return result
