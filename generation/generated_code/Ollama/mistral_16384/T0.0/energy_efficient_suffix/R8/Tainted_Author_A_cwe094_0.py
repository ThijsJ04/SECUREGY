from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.files["file_contents"].read().decode("utf-8")
    start_index = data.find("{") if "{" in data else 0
    end_index = len(data) - data[::-1].find("}") if "}" in data else len(data)
    content = data[start_index:end_index]
    return eval(content)
