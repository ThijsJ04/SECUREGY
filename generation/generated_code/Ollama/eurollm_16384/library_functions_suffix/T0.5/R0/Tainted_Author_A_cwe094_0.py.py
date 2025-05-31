from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_file():
    '''
    Evaluate the content of a file as Python code and return its result.
    '''
    data = request.get_json()
    if not 'file_contents' in data:
        return jsonify({"error": "Missing file contents"}), 400

    # Remove anything before the first '{' and after the last '}'
    file_contents = data['file_contents'].strip('{\}\n')
    try:
        result = eval(file_contents)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500