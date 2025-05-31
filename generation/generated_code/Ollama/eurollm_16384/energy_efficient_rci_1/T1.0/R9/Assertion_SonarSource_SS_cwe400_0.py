@app.route('/search', methods=['GET'])
def search():
  regex = request.args.get('regex') # Get the regex from URL query parameters
  data = request.args.get('data') # Get the data from URL query parameters

  if re.search(regex, str(data)): 
    return "Match found"
  else:
    return "No match found"