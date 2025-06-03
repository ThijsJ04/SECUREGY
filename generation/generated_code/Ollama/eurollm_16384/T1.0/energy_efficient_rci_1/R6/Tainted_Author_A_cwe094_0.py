from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def eval_dict():
    content = request.args.get("file_contents")
    if not content:
        return "No content provided", 400

    try:
        dict_data = eval(content[content.find("{") + 1 : content.rfind("}")])
        return str(dict_data), 200
    except Exception as e:
        return "Invalid dictionary format", 400
