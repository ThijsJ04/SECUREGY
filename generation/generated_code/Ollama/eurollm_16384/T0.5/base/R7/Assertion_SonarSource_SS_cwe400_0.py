import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    """
    Search for a regex pattern in the request body and return the result.
    """
    data = request.get_json()  # Get JSON data from request
    regex = re.compile(r"\d+")  # Regular expression to search for

    matches = regex.findall(data)

    if matches:
        return jsonify({"result": "Match found", "matches": matches})
    else:
        return jsonify({"result": "No match found"})


if __name__ == "__main__":
    app.run(debug=True)
