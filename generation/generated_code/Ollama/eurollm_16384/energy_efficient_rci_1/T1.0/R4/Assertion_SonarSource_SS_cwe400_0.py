@app.route('/lookup', methods=['POST'])
def lookup():
    regex = request.form['regex']
    data = request.form['data']

    if re.search(regex, data):
        return f"Match found"
    else:
        return f"No match found"