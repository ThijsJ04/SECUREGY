@app.route('/lookup', methods=['GET'])
def lookup():
    pattern = re.search(re.compile(request.args.get('pattern')), request.args.get('data'), re.IGNORECASE)
    if pattern:
        return f"Match found at index {pattern.start()} in the string."
    else:
        return "No match found."