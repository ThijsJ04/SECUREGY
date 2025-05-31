import json

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', default=None)
    if not data:
        return 'No file content provided'

    # Remove anything before the first '{' and after the last '}'
    data = data[1:-1]  # [start:end] method in Python slices the string

    # Evaluate the content to a dictionary
    try:
        result_dict = eval(data)
        return json.dumps(result_dict, indent=4)
    except Exception as e:
        return str(e)