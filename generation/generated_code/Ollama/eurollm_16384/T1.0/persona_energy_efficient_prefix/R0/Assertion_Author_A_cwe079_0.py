from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!"
    try:
        first_name = request.args.get("first_name", default=None)
        if not first_name:
            return make_response(
                f"No first name provided. Please pass 'first_name' in the query string.",
                400,
            )

        send_message = f"Greetings, {escape(first_name)}!"
    except ValueError as e:
        return make_response(str(e), 500)
    except Exception as e:
        return make_response(str(e), 500)

    return send_message
