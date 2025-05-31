@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name')  # Assuming the first name is passed in the URL as a query parameter named 'first_name'
    personalized_greeting = f"Greetings, {escape(first_name)}!" if first_name else "Hello!"
    return make_response(personalized_greeting)  # Return the greeting as a response to the user