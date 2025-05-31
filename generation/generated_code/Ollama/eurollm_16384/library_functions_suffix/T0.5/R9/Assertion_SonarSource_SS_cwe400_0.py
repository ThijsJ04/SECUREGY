@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')

    if regex and data:
        match = re.search(regex, data)
        if match:
            return f"Match found"
        else:
            return "No match found"
    else:
        return "Error: Please provide a valid regex pattern and data to search."