from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', type=str)

    # remove everything before the first '{' and after the last '}'
    start = file_contents.find('{') if '{'.in(file_contents) else 0
    end = file_contents.rfind('}') + 1 if '}' in file_contents else len(file_contents)
    content = file_contents[start:end]

    try:
        # evaluate the content as a dictionary
        return jsonify(eval(content))
    except Exception as e:
        return {'error': str(e)}, 400