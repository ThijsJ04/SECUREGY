from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.json["file_contents"]
    processed_content = file_contents.split("{", 1)[1].rsplit("}", 1)[0]
    result = eval(processed_content)
    return result
