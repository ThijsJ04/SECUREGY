def contents_dict(file_contents):
    try:
        # Remove everything before first '{' and after last '}'
        data = file_contents[1:-1]

        # Evaluate the string as a dictionary
        content = eval(data)
        return content
    except Exception as e:
        return str(e)