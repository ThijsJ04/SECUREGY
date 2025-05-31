def contents_dict():
    file_contents = request.args.get('file_contents', default=None, type=str)

    if file_contents is None or not file_contents:
        return {}, 400

    cleaned_json = file_contents[file_contents.find('{') : -1 * file_contents[-1:].rfind('}')]
    return json.loads(cleaned_json)