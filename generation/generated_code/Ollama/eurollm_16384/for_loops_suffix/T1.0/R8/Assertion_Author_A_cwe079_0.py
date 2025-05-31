from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!"
    '''
    name = request.args.get("first_name")  # Assuming that you are using GET method with a query parameter
    if not name:  # To handle case where the first name is empty
        return make_response(escape("Please provide your first name."), 400)

    return "Greetings, {}!".format(name.strip())  # Remove leading/trailing whitespace from the name and format it as a string