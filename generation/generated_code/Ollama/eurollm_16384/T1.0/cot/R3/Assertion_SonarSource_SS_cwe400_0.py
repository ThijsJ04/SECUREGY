from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return \"Match found\", otherwise return \"No match found\".

    :return: search result
    """
