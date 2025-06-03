from flask import Flask, request
from mimetypes import MIMETypes
import json
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.form["file_contents"]
    mime_types = MIMETypes()
    content_type, _ = mime_types.guess_type(file_contents)
    if content_type == "application/json":
        return json.loads(file_contents[file_contents.find("{") :])
    matched = re.match(r"^{(.*)}$", file_contents, re.DOTALL)
    if matched:
        return json.loads(matched.group(1))
    return None
