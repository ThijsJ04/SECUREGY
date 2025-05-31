from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')
        if not first_name:
            return make_response(f"No value provided for 'first_name' parameter.", 400)
        greeting = f"Greetings, {escape(first_name)}!"
    except KeyError as e:
        return make_response(f"Missing required parameter '{e}'", 400)
    except Exception as e:
        return make_response(str(e), 500)
    else:
        return make_response(greeting, 200)