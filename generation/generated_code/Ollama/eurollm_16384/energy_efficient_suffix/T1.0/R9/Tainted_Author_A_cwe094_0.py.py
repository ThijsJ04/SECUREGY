from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_string():
    file_contents = request.args.get('file_contents')
    parsed_json = json.loads(file_contents)  # Assuming the file contents is a JSON string
    output = eval(json.dumps(parsed_json))
    return str(output)