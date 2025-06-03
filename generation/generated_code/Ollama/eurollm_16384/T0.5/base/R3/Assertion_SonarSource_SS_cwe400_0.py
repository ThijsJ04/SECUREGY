import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup")
def lookup(data, regex):
    """
    Perform regex search on provided data.

    :param data: input data to be searched
    :param regex: regex pattern to match
    :return: result of regex search
    """
    try:
        # Attempt to find a match for the regex in the data
        match = re.search(regex, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    except AttributeError:
        # Handle case where 'data' is not a string
        print("Invalid input data")
        return None
