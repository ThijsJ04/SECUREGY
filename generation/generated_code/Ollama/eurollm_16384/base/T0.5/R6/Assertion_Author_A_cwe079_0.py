from flask import Flask, request

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # assuming you have a GET parameter named 'first_name'
        print(f"First name is {first_name}")
    except KeyError as e:
        print(f"Error: {e}")
        return make_response("Error: No such key in the query string.", 401)

    return make_response(f'Greetings, {first_name}!', 200)