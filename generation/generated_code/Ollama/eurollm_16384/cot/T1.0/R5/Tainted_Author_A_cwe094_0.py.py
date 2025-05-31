def contents_dict(data):
    # Remove everything before and after '{' characters
    content = ''
    for line in data.split('\n'):
        if '{' in line or '}' in line:
            content += line[1:] if line[0] == '{' else line[:-1] + ' '
        elif not line and len(content) > 0:  # Remove empty lines at the end
            return dict(eval(content))
    return None