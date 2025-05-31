from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content_data = request.data.decode('utf-8')
    start = content_data.find('{') + 1
    end = content_data.rfind('}')
    cleaned_content = content_data[start:end]
    result = eval(cleaned_content)
    return dict(result)

if __name__ == '__main__':
    app.run(debug=True)