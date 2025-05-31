@app.route('/lookup', methods=['GET'])
def lookup():
    try:
        regex = request.args.get('regex')
        data = request.args.get('data')
    except ValueError as e:
        return 'Invalid input format. Please provide regex and data in the URL query parameters.'

    if not regex or not data:
        return 'No input provided.'

    pattern = re.compile(regex)
    match = pattern.search(data)

    if match:
        return f'Match found at position {match.start()} in the string "{data}".'
    else:
        return 'No match found.'