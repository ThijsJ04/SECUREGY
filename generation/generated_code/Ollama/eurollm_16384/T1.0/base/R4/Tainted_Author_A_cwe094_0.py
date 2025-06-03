from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_data():
    data = request.get_json()
    content = str(data)
    file_contents = content[content.find("{") + 1 : content.rfind("}")]
    try:
        return jsonify({"result": eval(file_contents)})
    except Exception as e:
        return str(e), 500
