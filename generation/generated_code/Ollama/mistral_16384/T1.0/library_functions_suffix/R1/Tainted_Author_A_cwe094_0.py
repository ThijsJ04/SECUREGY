from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if file_contents:
        cleaned_json = file_contents[1:-1]  # remove leading and trailing '{' and '}'
        return json.loads(cleaned_json)  # return the content as a dictionary
