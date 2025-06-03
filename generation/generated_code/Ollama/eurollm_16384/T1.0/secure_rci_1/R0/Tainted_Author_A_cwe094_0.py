from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def eval_function():
    data = request.args[
        "file_contents"
    ]  # Get the data from the request using 'file_contents'.
    if not data:  # If the input is empty, return an error message.
        return "Error: Input file contents cannot be empty."

    result = (
        eval(data) if len(data) > 0 else {}
    )  # Evaluate the content to a dictionary and return it.
    return str(
        result
    )  # Return the result as a string, which might need to be modified according to your application's requirements.
