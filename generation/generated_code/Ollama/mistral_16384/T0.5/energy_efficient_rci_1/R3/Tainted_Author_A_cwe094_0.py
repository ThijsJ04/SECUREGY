from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start = file_contents.find("{") if "{".lower() in file_contents else 0
    end = (
        len(file_contents) - (file_contents[-1:].rfind("}") + 1)
        if "}" in file_contents
        else len(file_contents)
    )
    content = file_contents[start:end]
    try:
        return jsonify(eval(content))
    except Exception as e:
        return str(e), 500
