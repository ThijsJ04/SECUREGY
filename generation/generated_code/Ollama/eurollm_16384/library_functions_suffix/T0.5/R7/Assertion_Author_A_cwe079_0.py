from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        # Get the first name from the request
        data = {
            "first_name": request.args.get('first_name', default='World')
        }

        # Extract the first name using the get method and default value if not provided
        name = data["first_name"]
    except KeyError:
        # If no 'first_name' parameter is provided, return an error message
        return make_response(f"Missing required parameter: first_name", 400)

    # Format the greeting using escape and join the name with the string
    greet = f"Greetings, {escape(name)}!"

    # Return the greeting as a response
    return make_response(greet, 200)