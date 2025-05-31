@app.route('/lookup')
def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    match = bool(re.search(regex, data))
    return "Match found" if match else "No match found"