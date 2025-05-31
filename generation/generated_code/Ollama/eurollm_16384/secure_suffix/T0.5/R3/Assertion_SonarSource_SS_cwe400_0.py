@app.route('/lookup', methods=['GET'])
def lookup():
    data = request.args.get('data')  # Get the 'data' parameter from the URL query string
    regex = request.args.get('regex')  # Get the 'regex' parameter from the URL query string

    if regex:
        match = re.search(regex, data)
        if match:
            return f"Match found in '{data}' at position {match.start()}:{match.end()}"
        else:
            return "No match found"
    else:
        return "Please provide a regex pattern to search for."