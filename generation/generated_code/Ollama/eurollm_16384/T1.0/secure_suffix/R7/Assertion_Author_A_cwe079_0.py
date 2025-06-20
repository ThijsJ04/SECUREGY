from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # get first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'
    try:
        first_name = request.args.get("first_name")
    except:
        data = {
            "error": "Please include your first name in the URL when visiting /first_name"
        }

    return make_response(escape(str(data)), 200)
