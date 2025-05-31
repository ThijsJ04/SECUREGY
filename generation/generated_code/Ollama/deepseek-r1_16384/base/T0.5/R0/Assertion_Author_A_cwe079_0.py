from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name')
    if not first_name:
        response = make_response("Name not provided.", 400)
        return response
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting)