@app.route('/eval')
def contents_dict():
    data = request.form['file_contents']
    start, end = data.find('{'), data.rfind('}')
    content = data[start:end + 1]
    return json.loads(content)