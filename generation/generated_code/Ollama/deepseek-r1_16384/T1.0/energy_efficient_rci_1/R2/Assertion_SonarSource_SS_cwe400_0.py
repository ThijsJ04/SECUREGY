from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        # Attempt to get JSON data first
        try:
            data = request.get_json()
        except:
            # If JSON not present, fallback to form data
            data = request.form

        regex = data["regex"]
        text = data["data"]

        if re.search(regex, text):
            return {"result": "Match found"}
        else:
            return {"result": "No match found"}
    except (KeyError, ValueError) as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
