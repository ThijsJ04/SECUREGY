@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', None)
    if data is not None:
        data = data.strip('{}')
        try:
            return json.loads(data)
        except ValueError as e:
            # handle errors, e.g., returning an error message or an empty dict
            return {}