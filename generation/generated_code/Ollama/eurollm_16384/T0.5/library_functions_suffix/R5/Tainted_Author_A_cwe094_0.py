from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    file_contents = request.args.get(
        "file_contents"
    )  # Get the file contents from the URL query string
    data = (
        eval(file_contents) if "file_contents" in request.args else {}
    )  # Evaluate the string as a dictionary
    return str(data)
