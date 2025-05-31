import json
from flask import request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default='{}')  # Get the JSON string from the request URL or query parameters
    try:
        data = json.loads(file_contents)
        return json.dumps(data, indent=4)
    except json.JSONDecodeError as e:
        return str(e), 500