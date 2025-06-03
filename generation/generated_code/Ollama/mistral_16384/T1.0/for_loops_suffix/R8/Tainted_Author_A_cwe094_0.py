from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")

    # Remove anything before the first '{' and after the last '}'
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}") + 1
    json_string = file_contents[start_index:end_index]

    # Return the content by evaluating it to a dictionary
    return json.loads(json_string)
