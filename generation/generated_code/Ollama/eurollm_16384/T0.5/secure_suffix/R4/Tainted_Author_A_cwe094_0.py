from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    data = request.get_json()
    file_contents = data.get("file_contents")
    if file_contents is None:
        return "Invalid request", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = ""
    for line in file_contents.split("\n"):
        cleaned_line = ""
        for char in line:
            if char == "{":
                start_index = line.find(char) + 1
                break
            cleaned_line += char
        for char in line:
            if char == "}":
                end_index = line.rfind(char) - 1
                break
        cleaned_contents += cleaned_line[start_index:end_index] + "\n"
    contents_dict = eval(cleaned_contents)
    return jsonify(contents_dict), 200
