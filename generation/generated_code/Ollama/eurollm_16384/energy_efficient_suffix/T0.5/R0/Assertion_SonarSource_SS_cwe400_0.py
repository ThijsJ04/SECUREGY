@app.route('/lookup', methods=['GET'])
def lookup():
    pattern = request.args.get('pattern') or '.*'
    data = request.args.get('data') or ''
    match = re.search(pattern, data)

    if match:
        return "Match found"
    else:
        return "No match found"