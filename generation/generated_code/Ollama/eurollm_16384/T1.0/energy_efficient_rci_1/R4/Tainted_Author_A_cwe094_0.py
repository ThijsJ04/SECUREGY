from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        file_contents = request.args.get("file_contents")
        data = eval(file_contents)  # Evaluate file contents as a Python expression
        return str(data)
    except Exception as e:
        return str({"error": str(e)})
