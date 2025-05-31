from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Extract first_name from query parameters
    first_name = request.args.get('first_name', '')

    # Create greeting message
    if not first_name:
        greeting = "Greetings, Guest!"
    else:
        greeting = f"Greetings, {escape(first_name)}!"

    # Return response with appropriate headers
    return make_response(
        greeting,
        200,
        {
            'Content-Type': 'text/plain',
            'charset': 'utf-8'
        }
    )

if __name__ == '__main__':
    app.run(debug=True)