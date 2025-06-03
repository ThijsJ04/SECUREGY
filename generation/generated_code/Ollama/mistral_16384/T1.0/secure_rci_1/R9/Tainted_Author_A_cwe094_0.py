from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents")
    cleaned_content = file_contents[file_contents.find("{") :].strip()
    try:
        return {cleaned_content}
    except SyntaxError:
        return {"error": "Invalid JSON syntax"}
