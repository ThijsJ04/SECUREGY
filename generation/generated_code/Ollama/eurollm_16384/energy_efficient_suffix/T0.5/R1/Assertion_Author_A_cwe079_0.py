@app.route('/first_name')
def echo_name():
    name = request.args.get('first_name', default='World')  # get the first name if it exists, otherwise use 'World'
    return f"Greetings, {escape(name)}!"