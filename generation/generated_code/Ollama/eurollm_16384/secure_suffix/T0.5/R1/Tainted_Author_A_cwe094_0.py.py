from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    data = request.get_json()
    if 'file_contents' not in data:
        return "Error: Missing file contents field."

    content = data['file_contents']
    # Remove anything before the first '{' and after the last '}'
    content = content[content.find('{')+1:content.rfind('}')]

    try:
        result = eval(content)  # Evaluate the content to a dictionary
    except Exception as e:
        return str(e)

    return jsonify({'result': result})