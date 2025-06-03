from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Extract the input string from query arguments
    input_str = request.args.get("file_contents", "")

    # Find indices of first '{' and last '}'
    start = input_str.find("{")
    end = input_str.rfind("}")

    if start == -1 or end == -1:
        return {}  # Return empty dict if no valid JSON found

    # Extract the substring between braces
    json_str = input_str[start + 1 : end]

    try:
        # Evaluate the extracted string to a dictionary
        result = eval(json_str)
        return result
    except:
        return {}  # Return empty dict on evaluation errors
