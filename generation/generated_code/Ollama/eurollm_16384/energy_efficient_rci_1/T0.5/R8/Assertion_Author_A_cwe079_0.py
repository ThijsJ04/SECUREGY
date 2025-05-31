from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    args = request.args
    if 'first_name' not in args or len(args['first_name']) == 0:
        return make_response('Please provide your first name', 400)
    else:
        person = f"Greetings, {escape(args['first_name'])}!"
        return make_response(person, 200)