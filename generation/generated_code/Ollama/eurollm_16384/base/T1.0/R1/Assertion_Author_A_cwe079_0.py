from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    data = request.args.get("first_name")
    if data:
        greeting = f"Greetings, {escape(data)!r}!"
    else:
        greeting = "Hello there! How are you doing today?"

    return make_response(greeting)