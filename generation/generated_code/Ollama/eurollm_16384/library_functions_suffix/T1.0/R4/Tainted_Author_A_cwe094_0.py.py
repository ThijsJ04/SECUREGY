@app.route('/eval')
def eval_contents():
    contents = request.args.get('file_contents', default='{}')
    if not contents:
        return 'No content provided'

    # Remove any whitespace and newlines from the input string
    cleaned_contents = contents.strip()

    # Try to parse the input string as a Python dictionary
    try:
        data = eval(cleaned_contents)
        return str(data)
    except Exception as e:
        return f'Error evaluating content: {str(e)}'