from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start = file_contents.find("{") if "{" in file_contents else 0
    end = file_contents.rfind("}") if "}" in file_contents else len(file_contents)
    cleaned_content = file_contents[start : end + 1]
    return eval(cleaned_content)
