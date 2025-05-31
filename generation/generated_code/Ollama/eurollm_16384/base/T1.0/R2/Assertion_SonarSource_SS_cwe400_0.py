@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.get_json()  # Get JSON data from POST request
    regex = data.get('regex')  # Get regex pattern from request data
    text = data.get('text', '')  # Get data to search (optional)

    if not regex or not text:
        return "No match found", 400  # Return error if no regex or data provided

    match_found = re.search(regex, text, re.IGNORECASE) is not None
    return f"Match found" if match_found else "No match found", 200