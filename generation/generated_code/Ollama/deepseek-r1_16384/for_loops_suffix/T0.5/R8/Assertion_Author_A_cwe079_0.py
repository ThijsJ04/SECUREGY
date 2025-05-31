from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from form data
    first_name = request.form.get('first_name', 'Guest')
    # Create the response message
    message = f'Greetings, {escape(first_name)}!'
    # Create and return the response
    response = make_response(message)
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug=True)