from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents', '')
    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return {}

    cleaned_content = content[start+1:end]

    try:
        result_dict = eval(cleaned_content)
        return result_dict
    except:
        return {}

if __name__ == '__main__':
    app.run(debug=True)