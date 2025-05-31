@app.route('/eval', methods=['GET'])
def eval_contents():
    data = request.args.get('file_contents')
    if not data:
        return 'File contents not provided'

    try:
        content = data[1:-1]  # remove everything before the first '{' and after the last '}'
        result = eval(content)
        return str(result)
    except Exception as e:
        return f"Error evaluating contents: {e}"