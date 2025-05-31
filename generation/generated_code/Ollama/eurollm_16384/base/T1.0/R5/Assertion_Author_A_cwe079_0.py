@app.route('/first_name')
def echo_name():
    name = request.args.get('first_name', default='World')  # Default value is set to 'World' if not provided
    response = make_response(f"Greetings, {escape(name)}!")
    return response