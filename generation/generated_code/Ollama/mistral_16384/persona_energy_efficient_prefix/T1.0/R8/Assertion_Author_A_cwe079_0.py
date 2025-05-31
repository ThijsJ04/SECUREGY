@echo_name.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', None)
    if first_name is not None:
        response_msg = f'Greetings, {escape(first_name)}!'
    else:
        response_msg = 'No first name provided.'
    return make_response(response_msg)