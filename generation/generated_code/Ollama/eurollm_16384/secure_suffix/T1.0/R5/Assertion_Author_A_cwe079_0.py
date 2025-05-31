@app.route('/first_name')
def echo_name():
    data = request.args.get('first_name')
    if not data:
        return make_response(escape(u'Greetings, <empty>!'), 400)  # Return a response with an error message if no first name is provided
    return make_response(escape(u'Greetings, ' + escape(data)), 200)