from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    data = (
        file_contents[1:-1] if data.strip() else None
    )  # Remove any leading or trailing {}
    return (
        jsonify({"content": eval(data)}) if data else {"error": "Invalid JSON format"}
    )
