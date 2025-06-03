from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.form.get("file_contents", "")
    start = content.find("{")
    end = content.rfind("}")
    if start == -1 or end == -1:
        return jsonify({})
    cleaned = content[start + 1 : end]
    try:
        result = eval(cleaned)
        return jsonify(result)
    except:
        return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
