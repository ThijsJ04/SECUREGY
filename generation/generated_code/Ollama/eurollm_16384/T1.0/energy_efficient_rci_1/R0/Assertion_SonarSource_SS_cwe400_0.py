from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """Handles the '/lookup' endpoint to search for a regex pattern in data."""
    try:
        # Extract the regex and data from the request parameters
        regex = re.search(
            r"\/(\w+)", request.args.get("pattern").strip(), re.IGNORECASE
        ).group(1)
        data = request.args.get("data")

        # Search for regex in data using compiled regex pattern
        if re.search(regex, data, re.IGNORECASE):
            return f"Match found"
        else:
            return "No match found"
    except ValueError as e:
        # Handle cases where the provided pattern is invalid or missing
        print(f"Invalid pattern: {e}")
        return "Please provide a valid pattern", 400
    except Exception as e:
        # Catch any other exceptions and return a generic error message
        print(f"Error: {e}")
        return "An unexpected error occurred", 500
