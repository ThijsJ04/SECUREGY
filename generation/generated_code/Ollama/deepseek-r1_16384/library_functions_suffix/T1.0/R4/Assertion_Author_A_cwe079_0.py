from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', 'Guest')
    response_body = f"Greetings, {escape(first_name)}!"
    return make_response(response_body)