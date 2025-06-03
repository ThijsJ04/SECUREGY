from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    content_to_evaluate = file_contents[start + 1 : end]
    result = eval(content_to_evaluate)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
