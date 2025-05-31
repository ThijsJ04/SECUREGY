@app.route('/lookup', methods=['GET'])
def lookup():
    data = request.args.get('data')  # Get data from query parameter 'data'
    regex = request.args.get('regex')  # Get regex from query parameter 'regex'

    match_found = False
    pattern = re.compile(regex)

    for line in data.splitlines():
        if pattern.search(line):
            match_found = True
            print("Match found: " + line)
            break

    if not match_found:
        print("No match found")

    return "Match found" if match_found else "No match found"