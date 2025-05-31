@app.route('/lookup')
def lookup():
    regex = request.args.get('regex', default=None)
    data = request.args.get('data', default='no data provided')

    if regex is None:
        return 'No regex provided'

    match = re.search(regex, data)
    if match:
        return f"Match found: {match.group()}"
    else:
        return "No match found"