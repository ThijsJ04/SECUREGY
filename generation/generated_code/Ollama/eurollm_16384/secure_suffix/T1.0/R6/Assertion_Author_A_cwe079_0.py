from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""
    try:
        # Get the first name from the request parameters (e.g., GET query) or the data sent as part of a POST request
        args = dict(request.args)  # assuming the first name is in 'first_name' parameter for GET requests
        query_string = request.url.split('?')[1] if request.method == 'GET' else request.form.get('first_name', [])  # for POST requests or query strings without '?'
        args['first_name'] = escape(query_string) if 'first_name' in query_string else ''  # clean the input first name by escaping special characters and removing empty values
        first_name = args.get('first_name', [''])[0] # get only the first non-empty string from 'args'

        # Format and send back a response
        response = make_response(f"Greetings, {first_name}!")  # use escape to ensure HTML entities are properly escaped if the input includes special characters
        response.set_header('Content-Type', 'text/html')  # set Content-Type header for HTML output
        return response
    except Exception as e:
        return make_response("An error occurred: {}".format(e), 500)