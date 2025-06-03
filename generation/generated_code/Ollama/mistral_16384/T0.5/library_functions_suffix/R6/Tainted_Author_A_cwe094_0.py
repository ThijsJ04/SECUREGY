from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", type=str)
    cleaned_contents = (
        file_contents[file_contents.find("{") :] if "{" in file_contents else ""
    )
    cleaned_contents = cleaned_contents[: cleaned_contents.rfind("}") + 1]
    return eval(cleaned_contents)
