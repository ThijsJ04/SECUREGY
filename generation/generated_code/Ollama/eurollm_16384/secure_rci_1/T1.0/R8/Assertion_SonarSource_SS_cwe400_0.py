@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex') or None
    data = request.args.get('data') or None

    if regex is not None and data is not None:
        match = re.search(regex, data)
        if match:
            return 'Match found'
        else:
            return 'No match found'