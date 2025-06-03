import re


@app.route("/lookup", methods=["GET"])
def lookup():
    data = request.args.get("data")  # Assuming 'data' is a GET parameter
    regex = request.args.get("regex")  # Assuming 'regex' is a GET parameter

    if regex:
        match = re.search(regex, data)
        if match:
            return f"Match found"
        else:
            return "No match found"
    else:
        return "Please provide a valid regular expression and data to search."
