from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get("first_name")  # Assuming the first name is passed as a query parameter named "first_name"
    personalized_message = f'Greetings, {escape(first_name)}!' if first_name else 'Hello! No name provided.'
    return make_response(personalized_message.encode('utf-8'), 200)  # Returning the message as a response with HTTP status code 200