def evaluate_content(file_contents):
    try:
        # Remove anything before the first '{' and after the last '}'
        content = file_contents[file_contents.index('{') + 1:file_contents.rfind('}')]
        return eval(content)
    except Exception as e:
        # If there is an error, return None
        return None