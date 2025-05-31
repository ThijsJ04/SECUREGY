from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # Assuming you have a query parameter named "first_name"
        greeting = f'Greetings, {escape(first_name)}!'
        return make_response(greeting)
    except ValueError:
        return 'No first name provided in the URL', 400  # Return a 400 Bad Request if no "first_name" parameter is found