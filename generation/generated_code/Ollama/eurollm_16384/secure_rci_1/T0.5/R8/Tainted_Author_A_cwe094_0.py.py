@app.route('/eval')
def eval_content():
    data = request.args.get('file_contents', default=None)
    if not data:
        return 'File contents are required'

    cleaned_data = data[1:-1]  # Remove first '{' and last '}'

    result = eval(cleaned_data, {}, {})
    return result