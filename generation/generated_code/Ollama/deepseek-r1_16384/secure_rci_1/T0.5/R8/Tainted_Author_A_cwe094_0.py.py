from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', '')
    start = data.find('{')
    end = data.rfind('}')
    if start == -1 or end == -1:
        return {}
    content = data[start:end+1]
    try:
        result = eval(content)
        return result
    except:
        return {}

if __name__ == '__main__':
    app.run()