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
    file_contents = request.json.get('file_contents', '')

    # Extract substring between first { and last }
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'})
    content_str = file_contents[start+1:end]

    # Evaluate the string to a dictionary
    try:
        result_dict = eval(content_str)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)