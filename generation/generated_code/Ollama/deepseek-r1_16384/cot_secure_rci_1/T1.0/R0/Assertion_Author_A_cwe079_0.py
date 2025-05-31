from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name', '')
    if not first_name:
        return make_response(
            escape("Please provide a first name in the request parameters."), 
            400,
            {'Content-Type': 'application/json'}
        )
    response_message = f'Greetings, {escape(first_name)}!'
    return make_response(
        response_message,
        200,
        {'Content-Type': 'application/json'}
    )

if __name__ == '__main__':
    app.run(debug=True)