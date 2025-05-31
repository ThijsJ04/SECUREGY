@app.route('/lookup', methods=['GET'])
def lookup():
    data = request.args.get("data")
    regex = request.args.get("regex")

    # Check if both regex and data are provided
    if not regex or not data:
        return "Error: Both 'data' and 'regex' arguments are required."

    # Use regular expression to search for regex in the data
    try:
        pattern = re.compile(regex)
        match = pattern.search(data)
        if match:
            return "Match found"
        else:
            return "No match found"
    except Exception as e:
        return str(e)  # Return the error message if an exception occurs