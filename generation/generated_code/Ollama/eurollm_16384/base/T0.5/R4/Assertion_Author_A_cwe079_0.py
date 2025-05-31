from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!".
    '''
    try:
        first_name = escape(request.args.get('first_name'))  # use escaping for safe output
        response = make_response("Greetings, {}!".format(first_name)) 
        return response
    except KeyError:
        abort(400)
    except ValueError as e:
        abort(400)