from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # Get the first name from the URL path
        print(first_name)  # Print the first name for debugging purposes
    except KeyError as e:
        print("Please include 'first_name' in your URL path.")  # Handle the case where 'first_name' is not included
        make_response('Please include "first_name" in your URL path.')  # Return a response with error message
    else:
        content = f'Greetings, {escape(first_name)}!'  # Create the greeting message with escaped first name
        return make_response(content)  # Return the greeting message as a response