from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_contents():
    '''
    Evaluate the content of the file as Python code and return its result.
    '''
    data = request.args.get('file_contents')
    if not data:
        return 'No file contents provided', 400

    try:
        tree = ast.parse(data)
        result = eval(compile(tree, filename='', mode='eval'))
        return str(result)
    except Exception as e:
        return f"Error evaluating code: {str(e)}", 500