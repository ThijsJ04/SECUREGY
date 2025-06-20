from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Extract the file_contents parameter from the request
    file_data = request.args.get("file_contents", "")

    # Find the indices of the first '{' and last '}'
    start = file_data.find("{")
    end = file_data.rfind("}")

    if start == -1 or end == -1:
        return {}  # Return empty dict if braces not found

    # Slice the string to get content between the braces
    content = file_data[start + 1 : end]

    # Evaluate the content as a dictionary and return it
    try:
        return eval(content)
    except:
        return {}
