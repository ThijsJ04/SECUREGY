from flask import Flask, request
from mimetypes import MimeTypes
import json
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.data.decode("utf-8")
    # Remove anything before the first '{' and after the last '}'
    cleaned_json = re.sub(r"^{|}$", "", file_contents, flags=re.MULTILINE)
    try:
        return json.loads(cleaned_json)
    except ValueError as e:
        # Handle cases where the provided data cannot be parsed as JSON
        return str(e), 400


mime = MimeTypes()
app.add_url_rule("/eval", "application/json")(contents_dict)
