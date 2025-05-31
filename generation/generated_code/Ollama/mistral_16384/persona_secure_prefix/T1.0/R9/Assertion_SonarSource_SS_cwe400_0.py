def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    result = bool_to_text(regex.search(data))
    return result

def bool_to_text(bool_value):
    if bool_value:
        return "Match found"
    else:
        return "No match found"