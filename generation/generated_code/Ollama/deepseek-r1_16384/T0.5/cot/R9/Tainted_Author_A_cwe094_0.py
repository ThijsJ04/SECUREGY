from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")
    content_to_eval = file_contents[start_index + 1 : end_index]
    try:
        data_dict = eval(content_to_eval)
    except:
        return {}
    return data_dict
