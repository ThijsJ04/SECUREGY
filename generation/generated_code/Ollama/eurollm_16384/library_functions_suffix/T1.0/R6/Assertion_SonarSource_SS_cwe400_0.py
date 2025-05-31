@app.route('/lookup', methods=['POST'])
def lookup():
    regex = request.json.get('regex')
    data = request.json.get('data')

    if not regex:
        return "Missing regex", 400
    if not data:
        return "Missing data", 400

    for line in data:
        match = re.search(regex, line)
        if match:
            return f"Match found in line '{line}'"

    return "No match found"