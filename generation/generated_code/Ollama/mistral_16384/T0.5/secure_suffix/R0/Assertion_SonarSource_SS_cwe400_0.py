from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", "")
    data = request.args.get("data", "")
    result = re.search(regex, data)
    if result:
        return "Match found"
    else:
        return "No match found"


if __name__ == "__main__":
    app.run(debug=True)
