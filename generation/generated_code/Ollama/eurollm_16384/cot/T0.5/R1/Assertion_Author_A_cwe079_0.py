@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', default='World')  # Get the first name from the request using 'first_name' query parameter
    greeting = f"Greetings, {first_name}!"
    return make_response(greeting)