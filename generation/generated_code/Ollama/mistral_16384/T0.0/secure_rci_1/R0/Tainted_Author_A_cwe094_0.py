from flask import Flask, request
from mimetypes import MimeTypes
import json
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.files["file_contents"]
    content_type = MimeTypes().guess(file_contents.filename)
    if content_type == "application/json":
        return json.loads(file_contents.read().decode())
    match = re.search(r"{([^}]*)}", file_contents.read().decode())
    if match:
        return json.loads(match.group(1))
    else:
        return {"error": "Invalid JSON format"}
