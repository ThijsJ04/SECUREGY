@app.route('/lookup', methods=['GET'])
def lookup():
    try:
        # Get regex and data from request parameters
        regex = request.args.get('regex')
        data = request.args.get('data')
    except KeyError:
        return 'Error: Missing required arguments.', 400

    # Search for regex in data using regular expressions
    try:
        if re.search(regex, data):
            return 'Match found'
        else:
            return 'No match found'
    except re.error:
        return 'Error: Invalid regular expression.'