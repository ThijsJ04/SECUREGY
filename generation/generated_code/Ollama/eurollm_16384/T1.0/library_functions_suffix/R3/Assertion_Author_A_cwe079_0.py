from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    name = request.args.get(
        "first_name"
    )  # Assuming the 'first_name' query parameter is provided in the URL
    print("Name:", name)
    response = make_response(escape(f"Greetings, {name}!"))
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    return response
