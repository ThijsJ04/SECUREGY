from mimetypes import MIMETypes
import json
import io
from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.files["file_contents"]
    data = file_contents.read().decode("utf-8")
    start_index = data.find("{") + 1
    end_index = data.rfind("}")
    content = data[start_index:end_index]
    return json.loads(content)
