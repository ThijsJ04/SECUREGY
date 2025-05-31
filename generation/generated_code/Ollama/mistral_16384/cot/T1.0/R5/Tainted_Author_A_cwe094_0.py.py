from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return 'Error: No file_contents provided.', 400

    # Remove any characters before the first '{' and after the last '}'
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return 'Error: Invalid JSON structure.', 400

    formatted_json = file_contents[start:end + 1]
    try:
        json_dict = eval(formatted_json)
    except Exception as e:
        return f'Error: {str(e)}', 400

    return json_dict, 200