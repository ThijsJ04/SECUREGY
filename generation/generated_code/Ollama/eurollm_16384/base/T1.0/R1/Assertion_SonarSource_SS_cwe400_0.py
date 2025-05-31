@app.route('/lookup', methods=['GET'])
def lookup():
    pattern = request.args.get('pattern') or '.*'
    data = request.args.get('data') or 'no value given'

    if re.match(pattern, data):
        return f"Match found: {data}"
    else:
        return "No match found."