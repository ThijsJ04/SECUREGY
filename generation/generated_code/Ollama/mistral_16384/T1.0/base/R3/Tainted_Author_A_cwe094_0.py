from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    if file_contents:
        cleaned_string = file_contents[1:-1]  # remove surrounding {}
        try:
            return json.loads(cleaned_string)  # evaluate string to dictionary
        except json.JSONDecodeError as e:
            return str(e), 400
