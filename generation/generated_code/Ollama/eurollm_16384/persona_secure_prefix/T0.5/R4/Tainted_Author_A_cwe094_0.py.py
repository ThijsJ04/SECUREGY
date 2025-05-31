@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    try:
        # Get the file contents from the request
        data = request.args.get('file_contents')

        # Remove any leading or trailing whitespace
        data = data.strip()

        # Evaluate the string as a dictionary
        dict_data = eval(data)

        return str(dict_data)
    except Exception as e:
        return f'Error: {str(e)}', 500