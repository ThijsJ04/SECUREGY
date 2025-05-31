from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get("first_name")  # Assuming the first name is passed in via query parameters
    personalization = f'Greetings, {escape(first_name)}!' if first_name else 'Hello!'
    return make_response(personalization)