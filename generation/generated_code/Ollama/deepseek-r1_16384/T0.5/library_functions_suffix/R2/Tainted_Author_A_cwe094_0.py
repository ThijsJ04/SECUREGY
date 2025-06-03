from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input string from the request
    s = request.args.get("file_contents", "")

    # Extract substring between first '{' and last '}'
    start = s.find("{")
    end = s.rfind("}")
    if start == -1 or end == -1:
        return {}

    content = s[start + 1 : end]

    # Evaluate the content as a dictionary
    try:
        result = eval(content)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except:
        return {}


if __name__ == "__main__":
    app.run(debug=True)
