from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get('first_name') # assuming you have already defined the route for the '/first_name' URL endpoint
    except ValueError as e:
        status = 400  # return a 400 Bad Request response if no first name is provided in the request
        message = str(e) + ' Please provide a valid first name.' # send an error message with details about the error
    else:
        name = escape(first_name.strip())  # strip any leading or trailing whitespace from the input and replace any special characters
        status = 200                       # return a 200 OK response to indicate success
        message = f'Greetings, {name}!'    # send a message to the user with their name
    data = make_response(message, status)   # combine the message and status code into one Flask Response object
    return data