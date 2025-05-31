@app.route('/lookup')
def lookup():
    pattern = request.args.get('pattern', default='', type=str)
    data = request.args.get('data', default='data goes here', type=str)
    if not pattern:
        print("Pattern is required")
        return "Please provide a regex pattern"
    match = re.search(pattern, data)
    if match:
        return f"Match found at {match.start()}:{match.end()}"
    else:
        return "No match found"