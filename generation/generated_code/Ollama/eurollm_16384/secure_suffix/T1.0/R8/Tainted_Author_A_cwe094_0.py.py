from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_json():
    try:
        file_contents = request.args.get('file_contents')
    except KeyError as e:
        abort(400, description=f"Missing 'file_contents' parameter")

    data = file_contents.split("{")[1].split("}")[0]  # Get content after first '{' and before last '}'
    result = json.loads(data) if data else None
    return result