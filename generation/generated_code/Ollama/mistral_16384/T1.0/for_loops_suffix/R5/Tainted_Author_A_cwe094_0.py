from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """

    # Extract file_contents from the request
    file_contents = request.get_data(as_text=True)

    # Find the starting index of the opening brace '{' and ending index of the closing brace '}'
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")

    # Slice the string to remove unnecessary characters
    cleaned_content = file_contents[start_index : end_index + 1]

    # Evaluate the cleaned content as a Python dictionary
    return eval(cleaned_content)
