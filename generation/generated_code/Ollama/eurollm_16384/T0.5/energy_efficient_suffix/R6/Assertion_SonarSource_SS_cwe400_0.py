from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Search for a regex pattern in the data.

    :return: JSON response with "Match found" or "No match found"
    """
    try:
        # Get the regex pattern from request parameters
        pattern = re.compile(request.args.get("pattern"))

        # Get the data to search from request body
        data = request.json["data"] if "data" in request.json else []

        # Search for matches
        matches = [d for d in data if pattern.match(d)]

        # Return JSON response with results
        return jsonify(
            {
                "found": bool(
                    len(matches)
                ),  # True if at least one match found, False otherwise
                "matches": matches,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)})
