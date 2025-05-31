from flask import request, jsonify
import re

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_content():
    file_contents = request.form.get('file_contents')
    pattern = r'(?:^\{|\})(([^}]*)[\s\S]*?(?:\})|)(?!$)'
    match = re.search(pattern, file_contents)
    if match:
        # Remove everything before the first '{' and after the last '}'
        content = file_contents[match.start()+1:len(file_contents)-1]
        # Evaluate the content to a dictionary
        try:
            result = eval(content)
            return jsonify({'result': result})
        except Exception as e:
            print('Error evaluating content:', str(e))
            return 'Invalid syntax or content not valid for evaluation.'
    else:
        return 'No matching pattern found in the file contents.'