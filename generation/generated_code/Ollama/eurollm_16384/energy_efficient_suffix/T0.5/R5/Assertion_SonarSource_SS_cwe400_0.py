@app.route('/lookup', methods=['GET'])
def lookup():
    data = request.args.get('data')  # Assuming 'data' is the query parameter for the data to search in
    regex = request.args.get('regex')  # Assuming 'regex' is the query parameter for the regex pattern

    if not regex or not data:
        return "No match found", 400

    try:
        search_result = re.search(regex, data)
        if search_result:
            return f"Match found at index {search_result.start()} with length {len(search_result.group())}"
        else:
            return "No match found", 400
    except re.error as e:
        return str(e), 500