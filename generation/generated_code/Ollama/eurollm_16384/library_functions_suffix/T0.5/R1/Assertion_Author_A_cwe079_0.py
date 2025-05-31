from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # Get the first name from the request
        greeting = f"Greetings, {escape(first_name)}!" if first_name else "Hello!"  # Construct the greeting message
    except ValueError:
        print("No first name provided in the URL.")
        return make_response('No first name provided in the URL.', 400)  # Return a 400 error if no first name is provided
    else:
        return make_response(greeting, 200)  # Return the greeting message with HTTP status code 200