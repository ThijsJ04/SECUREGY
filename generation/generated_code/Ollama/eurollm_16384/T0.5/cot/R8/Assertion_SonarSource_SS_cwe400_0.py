import re
from flask import request, jsonify
from flask import Flask

app = Flask(__name__)

# Define a regular expression pattern for validating email addresses
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


def validate_regex(regex):
    """Validate a regex pattern."""
    try:
        return bool(re.compile(regex))
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return False


@app.route("/lookup")
def lookup(data):
    """Search for a match in the input data."""
    try:
        # Validate email addresses in the input data
        email_regex = re.compile(email_pattern, re.IGNORECASE)
        data = [email_regex.search(email).group() for email in data]
    except AttributeError:  # Handle non-string inputs
        print("Invalid input data.")
        return jsonify({"message": "Invalid input data"})

    # Search for a match using the specified regex pattern
    try:
        regex = re.compile(request.args.get("regex"), re.IGNORECASE)
        data = [regex.search(email).group() for email in data]
    except AttributeError:  # Handle missing or invalid regex argument
        return jsonify({"message": "Missing or invalid regex argument"})

    if not data:  # Check if any match is found
        return jsonify({"message": "No match found"})

    matches = [email for email in data if email]  # Filter out empty strings
    print(f"Match found: {', '.join(matches)}")
    return jsonify({"message": "Match found", "matches": matches})
