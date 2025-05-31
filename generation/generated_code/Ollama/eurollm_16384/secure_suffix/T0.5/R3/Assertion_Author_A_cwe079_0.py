from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    first_name = request.args.get('first_name')  # get the value of 'first_name' from the request URL
    personalized_greeting = f"Greetings, {escape(first_name)}!" if first_name else "Hello, stranger!"
    response = make_response(personalized_greeting)
    return response