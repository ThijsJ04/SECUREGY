from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.args.get("file_contents")
    if not data:
        return "Error: No file contents provided."

    try:
        content = eval(data)
        return str(content)
    except Exception as e:
        return f"Error: {str(e)}"
