from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_content():
    '''
    Evaluate the JSON content of the request and return it as a dictionary.
    '''
    data = request.get_json()
    if not 'file_contents' in data:
        return {'error': 'Missing file_contents key in JSON'}
    else:
        try:
            content = json.loads(data['file_contents'])
            # Remove everything before the first '{' and after the last '}'
            eval_content = {}
            for item in content:
                if isinstance(item, dict):
                    eval_content[item] = eval(json.dumps(item))
                else:
                    eval_content[item] = item
            return {'result': eval_content}
        except Exception as e:
            return {'error': str(e)}