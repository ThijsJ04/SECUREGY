from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def evaluate_file():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = {
        k: v
        for k, v in (
            item.split("=")
            for item in request.args.get("file_contents").strip().split("{")[1:-1]
        )
    }
    return str(data) + "}"
