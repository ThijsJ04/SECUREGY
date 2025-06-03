import re
from flask import request

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return matched text or "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        # Get regex and data from request
        pattern = request.json[
            "pattern"
        ]  # Assuming 'pattern' is the key for regex in JSON input
        data = request.json["data"]  # Assuming 'data' is the key for actual data

        if not isinstance(data, list) or any(
            not isinstance(item, str) for item in data
        ):
            return "Invalid data format. Please provide a list of strings."

        try:
            # Check if regex pattern is valid
            re.match(pattern, "test")  # Test regex validity
        except re.error as e:
            return f"Invalid regex pattern: {e}"

        # Search for the regex in data and return matched text or message
        matches = [
            m.group() if m else None for m in re.finditer(pattern, "".join(data))
        ]  # For Python 3.6+; use groupdict() with re.search() for earlier versions
        if matches:
            return (
                "Match found:" + "\n".join(matches)
                if len(matches) > 1
                else f"Match found: {matches[0]}"
            )  # For Python 3.6+; use groupdict() with re.search() for earlier versions
        else:
            return "No match found."
    except Exception as e:
        return str(e)  # Return error message if any exception occurs during processing
