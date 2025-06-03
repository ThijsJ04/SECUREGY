from flask import request
from flask import Flask
import re

app = Flask(__name__)


def lookup():
    regex = re.compile(request.args.get("regex"))
    data = request.args.get("data")
    match = re.search(regex, data)
    if match is not None:
        return "Match found"
    else:
        return "No match found"
