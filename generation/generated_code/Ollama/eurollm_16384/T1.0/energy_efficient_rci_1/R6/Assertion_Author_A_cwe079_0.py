from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    first_name = request.args.get("first_name")
    sentence = "Greetings, {}!".format(escape(first_name))
    return make_response(sentence)
