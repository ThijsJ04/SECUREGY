from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if file_contents is not None:
        cleaned_contents = '{' + file_contents.strip('{}') + '}'
        try:
            return jsonify(eval(cleaned_contents))
        except Exception as e:
            return str(e)