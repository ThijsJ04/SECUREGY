from flask import Flask, request
import ast, io

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers.get('file_contents', None)
    if not data:
        return '', 400

    # remove unnecessary characters from the start and end of the string
    data = data[data.find('{'):] if data.startswith('{') else data[data.index('{'):]
    data = data[:data.rfind('}') + 1]

    # evaluate the string as a python dictionary
    exec(f'dictionary = {data}', globals(), locals())
    return ast.literal_eval(io.StringIO(repr(dictionary)).getvalue()), 200