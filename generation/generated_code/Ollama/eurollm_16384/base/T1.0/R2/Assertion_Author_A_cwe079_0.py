from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    data = {'name': request.args.get('first_name', default='')}  # Assuming first_name is a URL parameter
    if not data['name']:  # Check if the name was provided in the URL
        return make_response(make_response("You didn't specify your first name", 400))
    else:
        greeting = f"Greetings, {escape(data['name'])}!" # escape prevents potential HTML injection issues
        return make_response(make_response(greeting, 200))  # Respond with the greeting