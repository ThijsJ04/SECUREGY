from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return {"error": "No file_contents provided"}
    start_index = file_contents.find("{") + 1
    end_index = file_contents.rfind("}")
    content_str = file_contents[start_index:end_index]
    try:
        data_dict = eval(content_str)
    except Exception as e:
        return {"error": str(e)}
    return data_dict
