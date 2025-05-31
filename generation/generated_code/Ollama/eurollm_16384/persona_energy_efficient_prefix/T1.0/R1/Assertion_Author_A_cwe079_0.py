from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = request.args.get("first_name")  # Assuming the first name is passed in the URL as a query parameter "first_name=<name>"
    print(name)  # Check if the first name was sent correctly
    return make_response('Greetings, ' + escape(name) + '!')  # Format the response with the escaped name