@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', default='World')  # Default value if not provided in query string
    greeting = f'Greetings, {escape(first_name)}!'
    return make_response(greeting)