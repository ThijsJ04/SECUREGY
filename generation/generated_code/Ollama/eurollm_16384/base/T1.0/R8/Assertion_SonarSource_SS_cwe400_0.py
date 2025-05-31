from flask import request, jsonify
import re

@app.route('/lookup', methods=['GET'])
def lookup():
    # Get regex and data from request
    pattern = request.args.get('pattern') or None
    data = request.form.to_dict() if 'data' in request.args else json.loads(request.values.get('data', ''))

    if not isinstance(data, dict):
        data = {k: v for k, v in zip(request.args.getlist('keys'), request.form)} if 'keys' in request.args else json.loads(request.values.get('data', ''))
        if not isinstance(data, dict):
            return "No match found", 400

    data = {k: v for k, v in zip(req.args.getlist('keys'), req.form)} if 'keys' in request.args else json.loads(request.values.get('data', ''))
    if not isinstance(data, dict):
        return "No match found", 400

    search_result = None
    for key, value in data.items():
        if pattern:
            if re.search(pattern, str(value)):
                search_result = {key: value}
                break

    return jsonify(search_result), 200 if search_result else 401