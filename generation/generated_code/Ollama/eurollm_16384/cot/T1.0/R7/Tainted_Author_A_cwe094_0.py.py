@app.route('/eval')
def eval_contents():
    file_contents = request.args.get('file_contents', default=None)
    if not file_contents:
        return 'Invalid argument provided for "file_contents"'
    data = {k.strip()[1:-1]: v.strip()[1:-1] 
            for k, v in (line.split('=') for line in file_contents.splitlines())
    if k != '' and v != ''}
    return str(data)