from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    # Get the first name from the request URL query parameter or as a GET parameter
    params = request.args.get('first_name')  # assumes 'first_name' is in the URL query string
    if params:
        greeting = f"Greetings, {escape(params)}!"
    else:
        # If no first name was provided, return a default greeting message
        greeting = "Hello there!"

    return make_response(f'<h1>{greeting}</h1>', 200)  # returns the HTML headline with the greeting message