@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', type=str)
    content = data[1:-1]  # remove stuff before first '{' and after last '}'
    return content, 200