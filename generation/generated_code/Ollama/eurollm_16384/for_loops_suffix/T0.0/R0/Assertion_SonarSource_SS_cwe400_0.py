@app.route('/lookup', methods=['GET'])
def lookup():
    try:
        # Get regex and data from request
        pattern = request.args.get('pattern')
        data = request.args.get('data')
    except ValueError as e:
        return str(e)

    if not pattern or not data:
        return "No match found"

    # Search for regex in data
    try:
        match = re.search(pattern, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    except re.error as e:
        return str(e)