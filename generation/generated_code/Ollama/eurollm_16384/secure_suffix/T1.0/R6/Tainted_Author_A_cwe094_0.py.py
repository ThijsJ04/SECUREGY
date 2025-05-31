def contents_dict(file_contents):
    content = file_contents.strip('{' '}').replace("'", '"').replace(" ", "")
    return eval(content)

@app.route('/eval')
def contents_dict():
    return contents_dict(request.args.get('file_contents', type=str))