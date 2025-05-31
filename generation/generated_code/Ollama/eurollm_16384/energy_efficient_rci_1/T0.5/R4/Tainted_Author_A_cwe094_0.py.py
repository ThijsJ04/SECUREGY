@app.route('/eval', methods=['GET'])
def eval_content():
    data = request.args.get('file_contents')
    if not data:
        return 'File contents is required'

    # Remove any whitespace at the beginning and end of the string
    data = data.strip()

    # Remove anything before the first '{' and after the last '}'
    start_index, end_index = 0, len(data) - 1
    while start_index <= end_index:
        if data[start_index] == '{':
            start_index += 1
            break
        start_index -= 1

    start_index, end_index = 0, len(data) - 1
    while start_index <= end_index:
        if data[end_index] == '}':
            end_index -= 1
            break
        start_index += 1

    data = data[start_index + 1:end_index]

    try:
        # Evaluate the string as a Python expression and return the result
        result = eval(data)
        return str(result)
    except Exception as e:
        # Return an error message if the evaluation fails
        return f'Error: {str(e)}'