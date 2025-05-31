def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    result = 'Match found' if bool(regex.search(data)) else 'No match found'
    return result