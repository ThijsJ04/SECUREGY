import re
from flask import request, jsonify

app = Flask(__name__)

# Global variable to store regex patterns for lookups
RE_PATTERNS = {}  # Empty dictionary to store regex patterns and data for each user


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        # Get the user's ID (replace '<user_id>' with the actual ID) and stored regex pattern from request parameters
        params = (
            request.args
        )  # Parse query string using `request.args` to get key-value pairs
        user_id = params["user_id"] if "user_id" in params else ""
        regex_pattern = re.compile(params["regex"]) if "regex" in params else None
        data = request.get_json()  # Get JSON-formatted data from the request payload

        if user_id and regex_pattern:
            match = None
            try:
                # Try to find a match between the regex pattern and data using `re.search` or `re.findall` depending on whether there's only one pattern in the regex string
                if (
                    "|" in regex_pattern
                ):  # Check if the regex pattern contains multiple patterns separated by '|' (e.g., 'a|b')
                    matches = [re.search(r, data) for r in regex_pattern.split("|")]
                    match = next(
                        (m for m in matches if m), None
                    )  # Return the first match found or `None` if none are found
                else:
                    match = re.search(regex_pattern, data)
            except (
                AttributeError
            ) as e:  # Handle cases when no regex pattern is provided for a user
                print(e)
                return "No match found"
        else:
            print("Invalid request")
            return "Invalid request", 400

        if match:
            result = (
                f"Match found in data '{data}' with regex pattern '{regex_pattern}'"
            )
        elif (
            not user_id and not regex_pattern
        ):  # Handle cases when no regex pattern is provided for a user
            print("No match found")
            result = "No match found"
        else:
            result = "Invalid request"

        return result, 200
    except (
        Exception
    ) as e:  # Catch any unexpected errors during the execution of the lookup function
        print(e)
        return str(e), 500
