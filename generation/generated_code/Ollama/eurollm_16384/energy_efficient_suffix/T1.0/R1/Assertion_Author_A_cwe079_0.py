from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        name = escape(request.args.get('first_name', ''))  # Escaping the input name to prevent XSS attacks
        print(f"Greetings, {name}!")
        return make_response("Greetings, " + name + "!")
    except Exception as e:
        return str(e)