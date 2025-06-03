from flask import request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        file_contents = request.args.get("file_contents")
        cleaned_content = file_contents[
            file_contents.find("{") + 1 : file_contents.rfind("}")
        ].strip()  # Remove leading and trailing whitespace
        result = eval(cleaned_content) if "eval" in request.args else cleaned_content
        return result
    except Exception as e:
        return str(e), 500
