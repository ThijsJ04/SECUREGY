import re

@app.route('/lookup')
def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    result = "Match found" if regex.search(data) else "No match found"
    return result