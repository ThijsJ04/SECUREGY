from flask import Flask, request
from mimetypes import MimeTypes
import json

mimes = MimeTypes()
mimes.add_type("application/json", ".json")

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.files["file_contents"].read().decode("utf-8")
    start_index = data.find("{") + 1
    end_index = data.rfind("}")
    content = data[start_index:end_index]
    return json.loads(content)
