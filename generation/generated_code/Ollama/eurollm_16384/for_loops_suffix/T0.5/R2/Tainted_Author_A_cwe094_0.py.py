from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    data = request.get_json()  # Assuming the request is in JSON format
    file_contents = data.get('file_contents')
    if file_contents:
        try:
            content = ast.literal_eval(file_contents)
            return str(content)
        except Exception as e:
            return f"Error: {str(e)}", 500
    else:
        return "Missing file contents", 400