def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    result = regex.search(data)
    if result:
        return "Match found"
    else:
        return "No match found"