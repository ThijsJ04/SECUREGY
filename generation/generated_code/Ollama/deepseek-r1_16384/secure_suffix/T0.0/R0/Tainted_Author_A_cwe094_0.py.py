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
    # Get the input string from form data
    content = request.form.get('file_contents', '')

    # Extract the substring between the first '{' and last '}'
    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return {'error': 'Invalid format'}
    cleaned_content = content[start+1:end]

    try:
        # Safely parse the content as JSON
        result = json.loads(cleaned_content)
        return result
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON'}, 400

if __name__ == '__main__':
    app.run(debug=True)