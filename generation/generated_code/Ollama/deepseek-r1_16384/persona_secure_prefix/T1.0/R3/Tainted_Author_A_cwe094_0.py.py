from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return jsonify({})
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}')
    if start_index == -1 or end_index == -1:
        return jsonify({'error': 'Invalid content format'})
    cleaned_content = file_contents[start_index+1:end_index]
    try:
        data_dict = ast.literal_eval(cleaned_content)
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()