from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # Get the first name from the request URL query string
        print(f"First Name: {first_name}")
    except KeyError:
        print("No 'first_name' parameter found in the URL query string.")
        return make_response("No 'first_name' parameter found.", 400)  # Return a 400 Bad Request response with an error message

    greeting = f"Greetings, {escape(first_name)}!" if first_name else "Hello!"
    return make_response(greeting, 200)  # Return the greeting as a JSON response