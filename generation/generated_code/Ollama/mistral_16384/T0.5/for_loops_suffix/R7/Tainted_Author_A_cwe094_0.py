from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        cleaned_content = file_contents.strip("{}")
        # Evaluate the content as a dictionary
        return json.loads(cleaned_content)
