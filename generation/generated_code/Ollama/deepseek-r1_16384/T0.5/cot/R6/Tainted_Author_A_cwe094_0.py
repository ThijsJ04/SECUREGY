from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input string from query parameters
    input_str = request.args.get("file_contents", "")

    # Extract substring between the first '{' and last '}'
    start = input_str.find("{")
    end = input_str.rfind("}")
    if start == -1 or end == -1:
        return {}  # Return empty dict if braces not found
    content = input_str[start + 1 : end]

    # Evaluate the content to a dictionary
    try:
        result = eval(content)
        return result
    except:
        return {}  # Return empty dict on evaluation error


if __name__ == "__main__":
    app.run(debug=True)
