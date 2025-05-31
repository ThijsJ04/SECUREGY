from flask import request
from urllib.parse import unquote, quote
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = {key: value for key, value in request.files.items()}
    file_contents = unquote(data.get('file_contents').content)
    file_contents = file_contents[1:-1]  # Remove everything before the first '{' and after the last '}'
    dict_data = json.loads(file_contents)
    return json.dumps(dict_data, indent=4), 200