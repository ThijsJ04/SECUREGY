from flask import Flask, request
import ast  # Using ast.literal_eval for safer evaluation

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', '')
    start = data.find('{')
    end = data.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'}), 400
    content = data[start:end+1]
    try:
        result = ast.literal_eval(content)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)