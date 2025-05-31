@app.route('/lookup', methods=['GET'])
def lookup():
    pattern = request.args.get('pattern')
    if not re.search(pattern, request.args.get('data')):
        return 'No match found'
    else:
        return 'Match found'