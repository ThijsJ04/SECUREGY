from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get("first_name")  # Assume first_name is a GET parameter
    salutation = "Hello, {}!".format(escape(first_name))  # Use escape to prevent XSS
    return make_response(salutation)  # Send back the response in JSON format. For HTML, you can use return make_response("{}".format(salutation), 200)