from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents', request.form.get('file_contents'))
    if not content:
        return jsonify({})

    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return jsonify({})

    expr = content[start+1:end]
    try:
        result = eval(expr)
        if isinstance(result, dict):
            return json.dumps(result)
        else:
            return jsonify({})
    except:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)