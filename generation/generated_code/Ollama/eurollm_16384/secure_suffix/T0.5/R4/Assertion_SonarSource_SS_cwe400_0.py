@app.route('/lookup', methods=['GET'])
def lookup():
    try:
        # Get regex and data from request
        regex = request.args.get('regex')
        data = request.args.get('data')
    except ValueError as e:
        return 'Invalid URL', 400

    # Search for regex in data
    if re.search(regex, data):
        return f'Match found'
    else:
        return 'No match found'