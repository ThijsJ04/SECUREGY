import json
from flask import request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Parse it to a JSON object and return it as a dictionary.
    """
    try:
        user_data = json.loads(request.args["file_contents"])
        content = (
            user_data[0] if isinstance(user_data, list) else user_data
        )  # handle case where input is a single value or string
        return jsonify({"result": content})
    except ValueError:
        return "Invalid JSON", 400
