from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name", None)
    if first_name is not None:
        response = make_response(f"Greetings, {escape(first_name)}!")
        response.mimetype = "text/plain"
        return response
    else:
        response = make_response("Invalid request format.", 400)
        response.mimetype = "text/plain"
        return response
