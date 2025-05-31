from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    name = request.args.get('first_name')  # Assuming 'first_name' is in the URL query string
    if name:
        greeting = f"Greetings, {escape(name)}!" if escape(name) else "Hello!"
        response = make_response(greeting)
        return response
    else:
        return 'No first name provided', 400