@app.route('/first_name')
def echo_name():
    data = request.args.get('first_name', default='world', type=str)
    greeting = f'Greetings, {escape(data)}!' if data else 'Welcome! (No name provided)'
    return make_response(greeting)