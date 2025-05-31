from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    first_name = request.args.get('first_name')  # Get the first name from the request parameters
    personalized_greeting = f"Greetings, {first_name}!" if first_name else "Hello, stranger!"
    response = make_response(personalized_greeting)
    response.set_cookie('welcome', value=personalized_greeting, path='/')  # Set a cookie to persist the greeting across requests
    return response