from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name')
    if not first_name:
        return make_response("First name is required", 400)
    response = f"Greetings, {escape(first_name)}!"
    return make_response(response, 200)

@app.route('/age')
def echo_age():
    '''
    Get the age from the request using 'age' and send it back to the user in this format: 'Your age is <age> years old.'.
    '''
    age = request.args.get('age', type=int)
    if not age:
        return make_response("Age is required", 400)
    response = f"Your age is {escape(age)} years old."
    return make_response(response, 200)