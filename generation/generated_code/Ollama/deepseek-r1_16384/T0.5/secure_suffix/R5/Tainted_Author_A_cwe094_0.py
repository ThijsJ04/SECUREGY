from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input data from the request
    file_contents = request.args.get("file_contents", "") or request.form.get(
        "file_contents", ""
    )

    # Extract the part between the first '{' and last '}'
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start != -1 and end != -1:
        content_to_eval = file_contents[start + 1 : end]
    else:
        return {}

    try:
        # Evaluate the extracted string as a dictionary
        result = eval(content_to_eval)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except Exception:
        return {}


if __name__ == "__main__":
    app.run(debug=True)
