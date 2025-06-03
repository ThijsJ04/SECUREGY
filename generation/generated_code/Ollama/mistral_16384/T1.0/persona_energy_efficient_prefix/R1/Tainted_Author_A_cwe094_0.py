from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.files["file_contents"]
    # Load the content as a string and remove unnecessary characters
    raw_data = str(data.read().decode("utf-8"))
    raw_data = raw_data[raw_data.find("{") + 1 : raw_data.rfind("}")]
    # Convert the string to a dictionary
    return json.loads(raw_data)
