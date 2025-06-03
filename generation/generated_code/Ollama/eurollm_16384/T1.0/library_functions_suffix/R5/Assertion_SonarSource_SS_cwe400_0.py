from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = None
    data = None

    # Get regex and data from the GET request
    regex_data = request.args.get("regex")
    data_data = request.args.get("data")

    if regex_data:
        regex = re.compile(regex_data)
    if data_data:
        data = data_data.lower()  # Convert to lowercase for case-insensitive search

    match = False
    for i in range(0, len(data), 2):
        if regex and (regex.search(data[i : i + 2])):
            match = True
            print("Match found")  # Print a debug message for demonstration purposes
            break
    else:
        print(
            "No match found"
        )  # Print another debug message for demonstration purposes

    return {"result": "match" if match else "no_match"}
