from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = request.args.get('first_name', 'Guest')  # Get query parameter or default to 'Guest'
    response_text = f'Greetings, {escape(name)}!'   # Format response with escaped name
    response = make_response(response_text)         # Create response object
    response.headers['Content-Type'] = 'text/plain'  # Set content type
    return response                                 # Return the formatted response