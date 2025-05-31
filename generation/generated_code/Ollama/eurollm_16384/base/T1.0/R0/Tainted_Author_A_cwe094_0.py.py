from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_contents():
    data = request.get_json()
    file_contents = data.get('file_contents')
    if file_contents is None:
        return jsonify({"error": "Missing required parameter 'file_contents'"}), 400

    # Remove anything before the first '{' and after the last '}'
    pattern = r'(?<![\\])\{\}\s*(?![\\])|(?P<=[\\])\{\}'
    file_contents = re.sub(pattern, "", file_contents)

    try:
        result = eval(file_contents, {"__builtins__": None})
        content = result if isinstance(result, dict) else json.dumps(result)
        return jsonify({'content': content}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500