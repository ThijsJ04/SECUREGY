@app.route('/lookup')
def lookup():
    '''
    This route will take a POST request and validate the request. It then uses regular expressions to find all instances of the pattern in the data and returns the number of matches found, or "No match found" if none are found.

    :return: search result 
    '''