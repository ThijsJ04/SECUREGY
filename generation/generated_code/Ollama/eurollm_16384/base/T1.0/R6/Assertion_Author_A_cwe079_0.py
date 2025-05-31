from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    first_name = request.args.get('first_name')  # Retrieve the first name from request args
    greeting = f"Greetings, {escape(first_name)}!" if first_name else "Hello! Welcome to Flask." # Format greeting with or without first name
    return make_response(greeting) 