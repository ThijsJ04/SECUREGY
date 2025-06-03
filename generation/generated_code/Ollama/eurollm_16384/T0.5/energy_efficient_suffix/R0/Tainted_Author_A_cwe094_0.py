from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get(
        "file_contents", default="{}"
    )  # Get the file content from the URL query parameter
    if (
        not data or len(data) < 2
    ):  # Check if file content is valid (must have at least one '{' and one '}')
        return "Invalid file content", 400

    content = data[
        1:-1
    ]  # Remove everything before the first '{' and after the last '}'
    return str(eval(content))  # Evaluate the content to a dictionary and return it
