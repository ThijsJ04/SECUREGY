from flask import request
from flask import Flask
import re

app = Flask(__name__)


def lookup():
    regex = re.compile(request.json["regex"])
    data = request.json["data"]
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
