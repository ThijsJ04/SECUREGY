from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # Assuming the first name is passed as a query parameter named "first_name"
        print(f'Got first name: {first_name}')
        response = make_response(f'Greetings, {escape(first_name)}!')
    except ValueError:
        response = make_response('Please provide a valid first name.')
    return response