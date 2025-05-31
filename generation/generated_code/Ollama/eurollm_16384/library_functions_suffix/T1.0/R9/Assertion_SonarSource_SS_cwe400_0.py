@app.route('/lookup')
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"