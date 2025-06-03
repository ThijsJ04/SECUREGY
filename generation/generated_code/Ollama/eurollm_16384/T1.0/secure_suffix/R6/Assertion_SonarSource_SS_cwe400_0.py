from flask import request, Response
import re

app = Flask(__name__)

# Sample data for testing purposes
DATA_EXAMPLES = [
    "Hello, World!",
    "Another line of text.",
    "123, 456, 789, 01234567890123456789",
    "(hello), (world!)",
    "\n(hello)\n(world!)\n",
]


@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.form["data"]  # Get data from form submission
    regex = request.args.get("regex")  # Get regex from query parameters

    # Convert data to string if it's a multipart/form-data request
    if "data" in request.files:
        data_file = request.files["data"]
        with open("./data.txt", "wb") as file:
            file.write(data_file.read())
        data = "data.txt"  # Store the file content in the 'data' variable
    elif isinstance(
        data, bytes
    ):  # Convert binary data to string if it's a POST request
        data = str(data)

    matches = []
    pattern = re.compile(regex or r".*", flags=re.IGNORECASE)  # Case-insensitive search

    for item in DATA_EXAMPLES:
        if pattern.search(data):
            matches.append({"item": item, "match": True})
            data = re.sub(
                pattern, r"\2", data
            )  # Replace all matches with a custom placeholder

    return Response(f"Match found in {len(matches)} items:", mimetype="text/plain")
