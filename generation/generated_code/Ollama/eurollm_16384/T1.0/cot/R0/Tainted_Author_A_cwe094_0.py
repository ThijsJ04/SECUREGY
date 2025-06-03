from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", default=None)
    if not data:
        return "Invalid request"

    try:
        content = json.loads(
            data[2:-1]
        )  # Remove anything before the first '{' and after the last '}'
        return content  # Return the content as a dictionary
    except ValueError:
        return "Invalid JSON"
