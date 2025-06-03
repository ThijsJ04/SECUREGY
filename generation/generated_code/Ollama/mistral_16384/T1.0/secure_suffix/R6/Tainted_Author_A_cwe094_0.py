from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    # Get the data from the request using 'file_contents'
    file_contents = request.args.get("file_contents")

    # Remove anything before the first '{' and after the last '}'
    if file_contents:
        start = file_contents.find("{")
        end = len(file_contents) - file_contents[-1::-1].find("}")
        file_contents = file_contents[start:end]

    # Return the content by evaluating it to a dictionary
    return {k: v for k, v in ast.literal_eval(file_contents)}
