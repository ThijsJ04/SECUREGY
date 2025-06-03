from flask import request
from flask import Flask
import re

app = Flask(__name__)


def lookup():
    try:
        # Get regex and data from request
        pattern = re.search(r"\/pattern", request.args.get("pattern")).group()
        data = request.args.get("data")

        # Search for regex in data
        if pattern in data:
            return f"Match found"
        else:
            return "No match found"
    except Exception as e:
        return str(e)
