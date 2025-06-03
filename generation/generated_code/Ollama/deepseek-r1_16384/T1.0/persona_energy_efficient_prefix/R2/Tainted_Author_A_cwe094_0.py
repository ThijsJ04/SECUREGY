from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents", "")
    # Extract content between first { and last }
    cleaned = file_contents.split("{")[1].rsplit("}", 1)[0]
    # Evaluate the cleaned string as a dictionary
    return eval(cleaned)


if __name__ == "__main__":
    app.run()
