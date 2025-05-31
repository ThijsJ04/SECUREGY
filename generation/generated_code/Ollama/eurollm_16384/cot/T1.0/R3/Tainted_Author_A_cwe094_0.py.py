def contents_dict():
    parsed_content = eval(request.args.get('file_contents').split('"')[1:-1])
    return str(parsed_content)  # or return the actual value instead of a string, depending on your requirements