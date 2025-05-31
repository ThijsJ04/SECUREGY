from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

def eval_file_contents(file_contents):
    '''
    Evaluates the given file contents as Python code and returns the result.
    '''
    try:
        # Remove anything before the first '{' and after the last '}'
        tree = ast.parse(file_contents[1:-1])
        result = eval(compile(tree, filename="<string>", mode="eval"))
    except Exception as e:
        return str(e)
    return result

@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()
    if not data or 'file_contents' not in data:
        return jsonify({"error": "Missing file contents"}), 400

    file_contents = data['file_contents']
    result = eval_file_contents(file_contents)
    return jsonify({'result': result})