from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    data = request.get_json()
    file_contents = data.get("file_contents")
    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        content = file_contents[1:-1]
        # Evaluate the content as a dictionary
        dict_content = eval(content)
        return json.dumps({"result": dict_content})
    else:
        return "Error: Missing 'file_contents' parameter."
