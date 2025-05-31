from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents', '')
    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'})
    cleaned_content = content[start+1:end]
    try:
        result = eval(cleaned_content)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)