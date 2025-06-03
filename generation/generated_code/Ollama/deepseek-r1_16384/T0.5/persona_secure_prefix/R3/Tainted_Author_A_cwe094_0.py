from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.form.get("file_contents", "")
    content = file_contents.split("{")[1].split("}")[0]
    content = content.replace("'", '"')  # Ensure quotes are properly escaped
    return eval(content)


if __name__ == "__main__":
    app.run(debug=True)
