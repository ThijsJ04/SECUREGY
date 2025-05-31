@app.route('/lookup', methods=['GET'])
def lookup():
    pattern = request.args.get('pattern')
    value = request.args.get('value')

    if not pattern or not value:
        return 'Please provide a regex and data to search for.'

    # Check if the input is valid (only one of pattern or value should be provided)
    if len(request.args.keys()) != 2:
        return 'Invalid request format. Please use GET method with two parameters: "pattern" and "value".'

    try:
        pattern = re.compile(pattern, re.IGNORECASE) if not pattern.isupper() else re.compile(pattern, 0)
        if value:
            return 'Match found in the following indexes: {}'.format('\n'.join([str(i) for i in pattern.finditer(value)]))
        else:
            return 'No match found.'
    except re.error as e:
        return str(e)