from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    try:
        first_name = escape(request.args.get('first_name'))
    except ValueError:
        abort(400, "Please provide a first name")

    response = make_response("Greetings, {}!".format(first_name))
    response.set_cookie('greeting', first_name)
    return response