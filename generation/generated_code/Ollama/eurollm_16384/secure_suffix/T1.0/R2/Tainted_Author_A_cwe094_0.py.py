from flask import request, jsonify

@app.route('/eval', methods=['POST'])
def eval_func():
    data = request.get_json()  # get JSON data from POST request
    file_contents = data.get('file_contents')  # get file contents from JSON data

    if file_contents:
        # remove whitespace and comments
        cleaned_contents = ''.join(line for line in file_contents if not (line.startswith('#') or line.isspace()))

        result = eval(cleaned_contents)  # evaluate the contents to a dictionary
    else:
        result = {}  # return an empty dictionary if no file contents are provided

    return jsonify({'result': result}), 200  # return the result as JSON with HTTP status code 200 (OK)