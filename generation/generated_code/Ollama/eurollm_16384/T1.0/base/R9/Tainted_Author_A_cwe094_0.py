from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.form["file_contents"]
    tree = ast.parse(
        data, mode="eval"
    )  # ast.parse() expects source code, but we have a string here
    # so we need the 'eval' mode for parsing Python code in a string
    return str(
        ast.literal_eval(str(tree))
    )  # now evaluate it to a string and then to dictionary
