from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    if request.method == 'POST':
        if 'file_contents' in request.form:
            content = request.form['file_contents']
        else:
            try:
                json_data = request.get_json()
                if isinstance(json_data, dict) and 'file_contents' in json_data:
                    content = json_data['file_contents']
                else:
                    return jsonify({'error': 'invalid data'}), 400
            except ValueError:
                return jsonify({'error': 'invalid json'}), 400
    else:
        content = request.args.get('file_contents')

    if not content:
        return jsonify({'error': 'file_contents missing'}), 400

    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1 or start > end:
        return jsonify({'error': 'invalid format'}), 400
    substring = content[start:end+1]

    try:
        result = ast.literal_eval(substring)
        if not isinstance(result, dict):
            raise ValueError("Result is not a dictionary")
    except (ValueError, SyntaxError) as e:
        return jsonify({'error': str(e)}), 400

    return jsonify(result)