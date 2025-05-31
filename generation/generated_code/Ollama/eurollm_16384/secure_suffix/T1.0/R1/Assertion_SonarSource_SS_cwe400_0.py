@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.form['data']  # get the data from the form
    regex = re.compile(request.form['regex'])  # compile the regex pattern

    if regex.search(data):
        return 'Match found'
    else:
        return 'No match found'