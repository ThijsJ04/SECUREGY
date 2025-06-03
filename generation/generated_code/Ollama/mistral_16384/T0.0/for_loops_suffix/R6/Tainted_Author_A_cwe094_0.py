from flask import Flask, request
from mimetypes import MimeTypes
import json
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.files["file_contents"]
    content_str = file_contents.read().decode("utf-8")
    start_index = content_str.find("{") + 1
    end_index = len(content_str) - content_str[::-1].find("}")
    cleaned_content = content_str[start_index:end_index]
    return json.loads(cleaned_content)
