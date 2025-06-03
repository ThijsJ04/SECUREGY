import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data") or "no_data_provided"

    if regex:
        # Validate input regex for basic syntax
        try:
            result = re.search(regex, data)
            print("Match found")
            return (
                "Match found" if result else None
            )  # or use 'No match found' instead of `None`
        except Exception as e:
            print("Invalid regex syntax", str(e))
            return "Invalid regex syntax"
    else:
        print("No regex provided")
        return "No regex provided"


if __name__ == "__main__":
    app.run(debug=True)
