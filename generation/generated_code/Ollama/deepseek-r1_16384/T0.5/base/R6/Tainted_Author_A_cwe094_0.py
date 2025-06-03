from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input string from form data
    s = request.form.get("file_contents", "")

    # Find indices of first '{' and last '}'
    start = s.find("{")
    end = s.rfind("}")

    # Extract substring between braces
    if start != -1 and end != -1:
        content = s[start + 1 : end]
    else:
        return {}  # Return empty dict if braces not found

    # Evaluate the content as a dictionary
    try:
        result = eval(content)
        return result
    except:
        return {}  # Return empty dict on evaluation error


if __name__ == "__main__":
    app.run(debug=True)
