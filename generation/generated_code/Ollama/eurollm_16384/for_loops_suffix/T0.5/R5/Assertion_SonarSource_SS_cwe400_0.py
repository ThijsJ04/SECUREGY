@app.route('/lookup', methods=['GET'])
def lookup():
    pattern = request.args.get('pattern')
    data = request.args.get('data')

    if re.search(pattern, data):
        return 'Match found'
    else:
        return 'No match found'