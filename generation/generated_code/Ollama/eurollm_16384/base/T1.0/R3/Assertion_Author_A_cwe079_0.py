from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Retrieve the first name from the request parameters
        data = request.args.get('first_name')
        if not data:
            return make_response("Error: Please provide a value for the 'first_name' parameter", 400)
    except ValueError as e:
        # Handle missing or incorrect data
        return make_response(str(e), 400)

    # Greet the user with their first name
    greeting = f"Greetings, {escape(data)}!" if data else "Hello!"  
    return make_response(greeting.encode('utf-8'))

if __name__ == '__main__':
    app.run()