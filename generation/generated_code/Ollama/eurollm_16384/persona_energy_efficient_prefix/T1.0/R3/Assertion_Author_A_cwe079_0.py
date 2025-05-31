from flask import Flask, request

app = Flask(__name__)

@app.route('/first_name', methods=['GET']) 
def echo_name():
    # get the first name from the 'first_name' key of the request arguments
    args = request.args
    first_name = args.get('first_name')

    if not first_name:
        return make_response(escape("Name is empty"))

    # return a response to the user in this format
    return make_response(escape("Greetings, {}!".format(first_name)))