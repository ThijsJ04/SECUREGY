from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get first_name from form data or query parameters
    first_name = request.form.get('first_name') or request.args.get('first_name')

    # Use escape() to prevent XSS attacks
    response_str = f'Greetings, {escape(first_name)}!' if first_name else 'Greetings, Guest!'

    # Return response with proper content type
    return make_response(response_str, 200, {'Content-Type': 'text/plain'})

if __name__ == '__main__':
    app.run(debug=True)