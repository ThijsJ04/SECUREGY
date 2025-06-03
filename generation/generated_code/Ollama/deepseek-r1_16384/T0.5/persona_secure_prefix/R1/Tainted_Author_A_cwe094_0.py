from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return "Bad request", 400
    # Extract content between first { and last }
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1 or start > end:
        return "Invalid format", 400
    content = file_contents[start + 1 : end]
    try:
        # Safely parse the content as a dictionary using json.loads
        data_dict = json.loads(content)
        return app.json.dumps(data_dict), 200
    except json.JSONDecodeError:
        return "Invalid JSON", 400


if __name__ == "__main__":
    app.run(debug=True)
