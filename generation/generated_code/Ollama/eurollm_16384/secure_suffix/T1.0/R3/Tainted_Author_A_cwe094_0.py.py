def contents_dict(request):
    data = request.args['file_contents']  # get the file content from the query string
    start = None
    end = len(data)
    while start is not None and end is not None:
        start, end = find_tag(data, '{')
        if start > 0:
            data = data[:start] + evaluate_expr(data[start:])  # replace the expression with its value
    content = dict() if 'content' in data else None
    return content