from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.form.get("file_contents")
    if not file_contents:
        return {}

    start_index = file_contents.find("{") + 1
    end_index = file_contents.rfind("}")

    if start_index <= 0 or end_index <= start_index:
        return {}

    content_str = file_contents[start_index:end_index]

    try:
        data_dict = eval(content_str)
        return data_dict
    except:
        return {}
