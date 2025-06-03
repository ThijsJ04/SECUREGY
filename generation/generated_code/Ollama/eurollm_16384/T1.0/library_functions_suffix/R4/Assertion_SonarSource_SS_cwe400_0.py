from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """Search for a regex pattern in the provided data."""
    pattern = request.args.get("pattern")  # Get the regex pattern from URL parameters
    text = request.args.get("text")  # Get the data to search in

    if not pattern or not text:
        return "Match not found", 400

    match_found = re.search(pattern, text)  # Search for the regex pattern in the text
    if match_found:
        return f"Match found: {match_found.start()} - {match_found.end()}"
    else:
        return "No match found", 200
