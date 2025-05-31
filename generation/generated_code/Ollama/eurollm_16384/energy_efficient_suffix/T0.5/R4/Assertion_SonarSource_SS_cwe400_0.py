@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.get_json()
    regex = data.get('regex')
    data_list = data.get('data')

    if regex and data_list:
        for item in data_list:
            if re.search(regex, item):
                return "Match found"
        return "No match found"
    else:
        return "Invalid input", 400