from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def eval_contents():
    data = request.get_data().decode("utf-8")
    file_content = "".join(
        [ch for ch in data if ord(ch) < 128 or (ord(ch) > 9 and ord(ch) < 10)]
    ).strip()
    try:
        return {k: eval(v) for k, v in file_content.split("{")[1].split("}").items()}
    except Exception as e:
        return "Invalid JSON format", 500
