from flask import Flask, request
import io

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    file_contents = request.args.get("file")
    data = file_contents.split("{")[0]  # Get the content before the first '{'
    data = eval(data) if "}" in data else data  # Evaluate the content to a dictionary
    return {"result": data}
