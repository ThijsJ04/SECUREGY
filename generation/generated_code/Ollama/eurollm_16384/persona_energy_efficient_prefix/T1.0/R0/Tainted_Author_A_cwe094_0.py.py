import json

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents')
    if not data:
        return 'No content provided.'

    try:
        content = eval(data)
        return json.dumps(content, indent=4)
    except Exception as e:
        return str(e), 500