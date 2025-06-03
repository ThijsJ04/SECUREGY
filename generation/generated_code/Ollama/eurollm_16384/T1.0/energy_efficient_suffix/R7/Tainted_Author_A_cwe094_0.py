from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    file_contents = request.form[
        "file_contents"
    ]  # Get the file content from the POST request
    decoded_string = file_contents.decode()  # Decode it to a string

    # Remove anything before the first '{' and after the last '}'
    cleaned_string = decoded_string[
        decoded_string.find("{") + 1 : decoded_string.rfind("}")
    ]

    # Evaluate the cleaned string to a dictionary
    result = eval(cleaned_string)

    return result  # Return the result as a JSON object
