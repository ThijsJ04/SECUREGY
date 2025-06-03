from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    if request.method == "GET":  # only do something if we are accessing by GET request
        first_name = request.args.get("first_name", default="World")
        data = {"name": escape(first_name)}
        resp = make_response(data)
    else:
        return "Error, please only send a request!"

    app.logger.info(f"Received first name: {first_name}")
    return resp
