from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", "")
    start_index = data.find("{")
    if start_index == -1:
        return jsonify({})
    end_index = data.rfind("}")
    content = data[start_index + 1 : end_index]
    try:
        result = eval(content)
    except:
        return jsonify({})
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
