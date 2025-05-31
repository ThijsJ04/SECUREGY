def contents_dict():
    # Get the data from the request using 'file_contents'
    file_contents = request.form['file_contents']

    # Remove anything before the first '{' and after the last '}'
    file_contents = file_contents[file_contents.find('{') : -file_contents[-1:].index('}')]

    # Return the content by evaluating it to a dictionary
    try:
        return eval(file_contents)
    except Exception as e:
        return str(e), 400  # Return an error message and status code if there's a problem with evaluation