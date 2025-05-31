@app.route('/eval', methods=['POST'])
def eval_content():
    data = request.get_json()  # Assuming JSON format
    file_contents = data.get('file_contents')

    if file_contents is None:
        return 'File contents not provided', 400

    # Remove everything before the first '{' and after the last '}'
    cleaned_content = file_contents[file_contents.index('{') + 1:file_contents.rfind('}')]

    # Evaluate the cleaned content to a dictionary
    result = eval(cleaned_content)

    return result, 200