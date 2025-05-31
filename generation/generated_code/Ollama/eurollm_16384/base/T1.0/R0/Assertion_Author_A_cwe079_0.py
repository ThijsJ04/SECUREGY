from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    # Extract the first name from the request using 'first_name' and store it in a variable called name
    name = request.args.get('first_name', default='guest', type=str)
    escaped_name = escape(name)  # encode special characters for proper display

    response = make_response(f"Greetings, {escaped_name}!")
    return response