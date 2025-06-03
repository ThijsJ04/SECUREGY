from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def evaluate_post_data():
    data = request.get_json()
    if not isinstance(data, dict):
        return {"error": "Not a valid JSON"}, 400

    content = ""
    for key, value in data.items():
        try:
            content += "%s={%s}\n" % (key, json.dumps(value))
        except ValueError as e:
            return {"error": str(e)}, 400
    content = content[:-1] + "\n}%"
    return {"result": eval(content)}, 200
