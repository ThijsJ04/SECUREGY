from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    try:
        # Get the first name from the request using 'first_name'
        first_name = request.args.get('first_name')
    except ValueError as e:
        return make_response(f"Invalid input: {str(e)}", 400)

    if not first_name:
        # Send the first name back to the user in this format
        return make_response('Greetings, {}!'.format(escape(first_name)), 200)