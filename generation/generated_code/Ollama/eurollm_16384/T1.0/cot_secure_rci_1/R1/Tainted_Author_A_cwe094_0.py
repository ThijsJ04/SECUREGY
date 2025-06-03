from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_contents():
    if request.method == 'GET':
        file_path = '/some/directory/with/your/file.txt'  # replace with your file path
        try:
            with open(file_path, 'r') as f:
                contents = f.read()
                # Assuming the file contains a valid JSON or dictionary string
                if contents.strip().startswith('{{'):
                    eval(contents)  # Evaluate as a Python expression
                else:
                    dict_data = eval(contents.split('}')[0))  # split by last '}' and remove leading whitespaces from first part
        except FileNotFoundError or PermissionError:
            return "File not found or permission denied", 404
    return ""