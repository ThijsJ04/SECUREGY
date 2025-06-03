from flask import Flask, request
from mimetypes import MimeTypes
import json
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.files["file_contents"].read().decode("utf-8")
    start_index = file_contents.find("{") + 1
    end_index = len(file_contents) - file_contents[-1:].rfind("}")
    content = file_contents[start_index:end_index]
    return json.loads(content)
