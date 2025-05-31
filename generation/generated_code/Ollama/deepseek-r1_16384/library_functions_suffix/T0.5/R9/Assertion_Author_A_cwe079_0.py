from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Extract first_name parameter from request arguments
    first_name = request.args.get('first_name', '')
    # Create greeting message with escaped name for safety
    greeting = f'Greetings, {escape(first_name)}!'
    # Prepare and send the response with appropriate headers
    response = make_response(greeting)
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug=True)