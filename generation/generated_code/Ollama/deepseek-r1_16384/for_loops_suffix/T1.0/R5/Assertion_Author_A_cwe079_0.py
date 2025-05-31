from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = request.args.get('first_name', '')  # Get first_name query parameter
    response_str = f"Greetings, {escape(name)}!"  # Escape special characters for safety
    return make_response(response_str, 200, {'Content-Type': 'text/plain'})