 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default=None)
    if file_contents:
        # Remove leading and trailing '{' and '}' if present
        file_contents = file_contents[1:-1] if file_contents.startswith('{') and file_contents.endswith('}') else file_contents

        try:
            # Convert the remaining string into a dictionary using json.loads()
            return {'status': 'success', 'data': json.loads(file_contents)}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}