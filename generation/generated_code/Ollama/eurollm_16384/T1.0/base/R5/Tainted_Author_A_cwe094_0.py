from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    data = request.args.get("file_contents")
    if not data or len(data) == 0:
        return "Missing required argument: file_contents"

    content = data[1:-1]  # Remove first '{' and last '}'
    result = eval(content, {"__builtins__": None})

    return result
