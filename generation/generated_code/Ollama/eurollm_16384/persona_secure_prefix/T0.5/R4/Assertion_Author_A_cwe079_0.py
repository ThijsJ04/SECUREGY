from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    data = {
        'first_name': request.args.get('first_name', default='World')  # get the first name from query parameters if not provided
    }
    response = make_response(f"Greetings, {escape(data['first_name'])!r}!")
    response.headers["Content-Type"] = "text/html; charset=utf-8"  # set the content type to html for easier parsing by browsers
    return response