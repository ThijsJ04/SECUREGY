from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    data = request.args.get('first_name')  # Get the value of 'first_name' as a string
    if not data:
        return make_response(escape("No first name provided"), 400)  # Return error if no first name is provided
    else:
        person = f"Greetings, {data}!"  # Format the greeting with the first name
        return make_response(person.encode('utf-8'), 200)  # Return the greeting as a response