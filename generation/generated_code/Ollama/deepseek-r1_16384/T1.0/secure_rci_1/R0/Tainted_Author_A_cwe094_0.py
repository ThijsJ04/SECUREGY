from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Extract the 'file_contents' parameter from the request
    file_contents = request.args.get("file_contents") or request.form.get(
        "file_contents"
    )

    # Find the index of the first '{' and last '}'
    start = file_contents.find("{")
    end = file_contents.rfind("}")

    # Slice the string to get only the content between '{' and '}'
    content_between = file_contents[start : end + 1]

    # Evaluate the content as a dictionary
    result_dict = eval(content_between)

    return result_dict
