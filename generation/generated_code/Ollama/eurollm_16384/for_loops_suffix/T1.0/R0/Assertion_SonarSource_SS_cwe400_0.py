from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    try:
        # Get regex and data from request
        pattern = request.args.get('pattern')
        text = request.args.get('text')

        # Check if both regex and text are provided
        if not (pattern and text):
            return 'Please provide both regex and text for lookup'
    except KeyError as e:
        return f"Missing key '{e}' in the request. You can use GET parameters like this: {'?' + ('&' + 'pattern=' + request.args.get('pattern') if 'pattern' not in request.args else '') + (request.args.get('text', default=None) or '')}"
    except Exception as e:
        return f"Error: {str(e)}"

    try:
        pattern = re.compile(pattern)
    except re.error as e:
        return str(e) if 'invalid syntax' in str(e)[:4] else "Invalid regex pattern."

    if not text or len(text) == 0:
        return 'Please provide a non-empty text for lookup.'

    try:
        text = re.sub(pattern, '', text).strip()  # Remove all matches and return new string after matching with regex
    except TypeError as e:
        return str(e) if "no match found" in str(e)[:3] else f"No match found."

    if len(text.split('\n')) == 0 or text.strip() == '':
        return 'Please provide a non-empty text for lookup.'
    elif pattern and not re.search(pattern, text):
        return "No match found."
    else:
        return f"Match found: {repr(list(set([word.strip() for word in re.split('\s+', str(text).lstrip().rstrip()) if len(str(word)) > 0])))}"