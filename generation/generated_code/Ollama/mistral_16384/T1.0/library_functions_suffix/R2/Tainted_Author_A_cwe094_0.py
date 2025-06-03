from mimetypes import MIMETypes
import json, io

from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.files["file_contents"].read()
    buffer = io.StringIO(data.decode())
    mime = MIMETypes().guess_type(data)[0]
    if mime != "application/json":
        return "Error: Content is not a valid JSON.", 400

    result = json.load(buffer)
    return jsonify(result)
