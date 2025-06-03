from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def evaluate_data():
    file_contents = request.form[
        "file"
    ]  # Assuming 'file' is the key for the file content in POST data
    try:
        with open(file_contents) as f:
            data = f.read()
        parsed_data = json.loads(
            data[data.find("{") + 1 : data.rfind("}")]
        )  # Find the first '{' and last '}' to get the dictionary content
        return str(parsed_data)
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Invalid JSON data."
