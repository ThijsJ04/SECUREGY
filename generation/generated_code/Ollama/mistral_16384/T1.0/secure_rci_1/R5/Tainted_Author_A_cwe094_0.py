from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)

    if not file_contents:
        return {"error": "No 'file_contents' provided."}, 400

    start = file_contents.find("{") + 1
    end = (
        len(file_contents) - 1 if file_contents[-1] == "}" else file_contents.rfind("}")
    )

    if start > end:
        return {"error": "Invalid JSON format."}, 400

    try:
        return {"content": eval(file_contents[start:end])}
    except Exception as e:
        return {"error": str(e)}, 400
