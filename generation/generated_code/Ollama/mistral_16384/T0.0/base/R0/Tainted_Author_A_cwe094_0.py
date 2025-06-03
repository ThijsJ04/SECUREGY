import marshal
from flask import Flask, request
from mimetypes import MIMETypes
import json
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.files["file_contents"]
    content_type = MIMETypes().guess(file_contents.filename)
    if content_type == "application/json":
        return json.loads(file_contents.read().decode())
    else:
        match = re.search(r"{.*}", file_contents.read(), re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            raise ValueError("Invalid JSON format")
