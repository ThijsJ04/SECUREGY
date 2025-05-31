from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_contents():
    data = request.args.get('file_contents')
    if not data:
        return 'Error: Missing file contents parameter.'

    try:
        content = data[1:-1]  # Remove characters before the first '{' and after the last '}'
        result = eval(content)
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating content: {str(e)}"