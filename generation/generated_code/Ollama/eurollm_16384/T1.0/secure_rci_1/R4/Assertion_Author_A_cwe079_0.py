from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    if "first_name" not in request.args or request.args["first_name"] is None:
        return make_response("Please provide a value for first_name", 400)
    args = {key: request.args[key] for key in ["first_name"]}
    return make_response(f"Greetings, {escape(args['first_name'])}!", 200)


if __name__ == "__main__":
    app.run()
