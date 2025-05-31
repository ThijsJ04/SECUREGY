from flask import request, jsonify
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get("regex") or ""
    data = request.args.get("data", [], "+") | set(request.args.get("data-as-string")) if isinstance(request.args.get("data"), str) else list(request.args.get("data")) 
    matches = {m.start() for m in re.finditer(regex, data)}  # matches will be set in this loop
    print(f'Data: {data}')
    print(f'Match Found? {any(m > 0 for m in matches)}')
    return jsonify({"found": any(m > 0 for m in matches)}) # jsonify will return '{"found": True}' or '{"found": False}'