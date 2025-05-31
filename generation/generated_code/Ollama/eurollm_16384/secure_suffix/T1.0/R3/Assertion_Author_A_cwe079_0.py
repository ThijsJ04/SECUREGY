from flask import Flask, request
import urllib.parse

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the GET parameters using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    params = request.args
    if 'first_name' not in params:
        return make_response(escape('No first name provided.'), 400)  # Return a 400 Bad Request response if no 'first_name' parameter is present

    return make_response(f'Greetings, {params["first_name"]}!', 200)