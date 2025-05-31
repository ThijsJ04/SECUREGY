@app.route('/first_name')
def echo_name():
    # Get the first name from the request using 'first_name'
    args = request.args
    if 'first_name' in args:
        first_name = str(args['first_name'])
        print("First Name:", first_name)
        return make_response(f"Greetings, {first_name}!")
    else:
        return "No first name provided."