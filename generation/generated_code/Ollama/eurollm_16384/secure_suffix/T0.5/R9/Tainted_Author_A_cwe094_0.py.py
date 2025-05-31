@app.route('/eval', methods=['POST'])
def eval_content():
    data = request.get_json()
    file_contents = data.get('file_contents')
    if not file_contents or '{' not in file_contents:
        return "Error: Invalid file contents"
    result = eval(file_contents)
    try:
        print(result)
    except Exception as e:
        return f"Error evaluating content: {e}"
    return str(result)