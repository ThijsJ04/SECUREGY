def contents_dict():
    file_contents = request.form['file_contents']
    start_idx = file_contents.index('{') + 1 if '{', in file_contents else 0
    end_idx = len(file_contents) - 1 if '}' in reversed(file_contents) else len(file_contents)

    content = file_contents[start_idx:end_idx]
    return eval(content)