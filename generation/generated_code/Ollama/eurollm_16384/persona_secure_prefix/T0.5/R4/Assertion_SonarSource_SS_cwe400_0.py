@app.route('/lookup', methods=['GET'])
def lookup():
    try:
        regex = request.args.get('regex')
        data = request.args.get('data')
    except ValueError as e:
        return 'Invalid input. Please provide regex and data.'

    if not regex or not data:
        return 'No input provided.'

    try:
        match = re.search(regex, data)
        if match:
            return f'Match found in "{data}".'
        else:
            return 'No match found in "{data}".'
    except re.error as e:
        return f'Error: {e}. Please check your regex pattern.'