@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', default='World', type=str)  # Get first name from query string, with a default value of 'World' if not specified
    response = make_response(f"Greetings, {escape(first_name)}!")
    return response