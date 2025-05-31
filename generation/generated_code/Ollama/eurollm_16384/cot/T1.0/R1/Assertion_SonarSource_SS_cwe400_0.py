@app.route('/lookup')
def lookup():
    regex = request.args.get('regex', default='example regex pattern')  # Get the regex from query parameters (optional)
    data = request.get_json() or request.args.get('data', default={})  # Get JSON data from query parameters (optional)

    if 'regex' in request.args:  # If a regex is provided as a query parameter, use it instead of using the JSON data's 'regex' key
        regex = request.args['regex']
        del request.args['regex']  # Remove the 'regex' key from the query parameters dictionary to avoid repetition
    elif 'data' in request.args:  # If JSON data is provided as a query parameter, use its 'regex' key if available
        if 'regex' in request.get_json():
            regex = request.get_json()['regex']
            del request.args['data']  # Remove the 'data' key from the query parameters dictionary to avoid repetition
    else:  # Fallback to using a hardcoded regex pattern if neither query parameter nor JSON data is provided
        regex = 'example regex pattern'

    try:
        found_matches = re.findall(regex, str(data))
        print('Match found')
    except AttributeError:  # Handle cases where the input is not a string or the regex does not match
        print('No match found')