@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', default=None)
    if not data:
        return 'Error: No file_contents provided'

    try:
        content = eval(data, {}, {"__builtins__": None})
        return str(content)
    except Exception as e:
        return f'An error occurred: {str(e)}'