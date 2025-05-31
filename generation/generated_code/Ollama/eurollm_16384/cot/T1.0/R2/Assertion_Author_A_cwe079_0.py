@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', default='World')  # Default value for first_name if it's not provided in the URL
    phrase = f"Greetings, {first_name}!"
    return make_response(phrase)