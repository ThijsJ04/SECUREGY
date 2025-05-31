def lookup(regex, data):
    """
    Search for regex in the given data and return a message.

    :param regex: The regex pattern to search for
    :type regex: str
    :param data: The text to search in
    :type data: str
    :return: A string indicating whether a match was found or not
    """
    try:
        # Remove newline characters from the regex pattern
        regex = re.compile(r'\b' + re.escape(regex) + r'\b')

        if regex.search(data):
            return "Match found"
        else:
            return "No match found"
    except AttributeError:
        # Handle the case when the input data is empty
        print("Input data cannot be empty.")
        return "Invalid input"

@app.route('/lookup', methods=['GET'])
def lookup_regex(request):
    """
    Get regex and data from request, perform the lookup, and return result.

    :param request: The current HTTP request
    :type request: Request object
    """
    return lookup(req.args.get('regex'), req.form.get('data'))