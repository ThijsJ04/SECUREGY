def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')

    if regex.search(data):
        return "Match found"
    else:
        return "No match found"