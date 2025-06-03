import json
from flask import request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")  # Get the data from the request
    try:
        if file_contents.startswith("{"):
            file_contents = file_contents[
                1:-1
            ]  # Remove anything before '{' and after '}'
    except ValueError:
        pass

    try:
        data = json.loads(file_contents)  # Try to parse it as JSON
        return str(data)
    except Exception as e:
        return f"Failed to parse JSON: {e}"
