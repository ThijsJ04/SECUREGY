def lookup(regex):
    try:
        # Extract data from request
        data = request.args.get('data')

        # Check if regex matches the data
        if re.search(regex, data):
            return f"Match found"
        else:
            return "No match found"
    except Exception as e:
        return str(e)