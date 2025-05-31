@app.route('/eval')
def eval_contents():
    data = request.args.get('file_contents', default='{}')  # Use default value if not provided
    if not data:  # If no file contents are provided, return 404 error message
        return 'File contents not found'

    try:
        content = eval(data)  # Evaluate the string as a Python expression
        return str(content)  # Convert the dictionary to a string and return it
    except Exception as e:
        return f"Error evaluating file contents: {str(e)}"