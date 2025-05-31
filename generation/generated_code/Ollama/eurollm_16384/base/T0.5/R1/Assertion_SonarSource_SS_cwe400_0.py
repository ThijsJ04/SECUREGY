@app.route('/lookup')
def lookup():
    pattern = request.args.get('pattern', default='', type=str)
    data = request.args.get('data', default='test string', type=str)
    if re.search(pattern, data):
        return 'Match found'
    else:
        return 'No match found'