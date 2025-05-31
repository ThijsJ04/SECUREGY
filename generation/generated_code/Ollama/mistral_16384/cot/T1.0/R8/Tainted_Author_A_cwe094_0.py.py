def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return {}, 400

    start = file_contents.find('{') + 1
    end = file_contents.rfind('}')

    if start == -1 or end == -1 or start > end:
        return {}, 400

    return eval(file_contents[start:end]), 200