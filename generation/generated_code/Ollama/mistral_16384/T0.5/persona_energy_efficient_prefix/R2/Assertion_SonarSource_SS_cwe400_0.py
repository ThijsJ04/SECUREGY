import re


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """

    # Extract the regex pattern from request parameters
    regex_pattern = (
        re.compile(request.args.get("regex")) if "regex" in request.args else None
    )

    # Get the data to search from the request body
    data = request.get_json()["data"]

    # Search for the pattern in the data and return the result
    if regex_pattern and re.search(regex_pattern, data):
        return "Match found"
    else:
        return "No match found"
