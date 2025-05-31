@app.route('/first_name')
def echo_name():
    if 'first_name' in request.args:
        first_name = request.args['first_name']
        return f"Greetings, {escape(first_name)}!"