from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.form.get('file_contents', '')
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    cleaned = file_contents[start+1:end]

    try:
        return json.loads(cleaned)
    except:
        return {}

# To run the application, you can use:
if __name__ == '__main__':
    app.run(debug=True)