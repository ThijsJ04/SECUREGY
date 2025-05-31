@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')

    if regex and data:
        match = re.search(regex, data)
        if match:
            return f"Match found in '{data}': {match.group()}"
        else:
            return "No match found"
    else:
        return "Invalid request. Please provide regex and data parameters."