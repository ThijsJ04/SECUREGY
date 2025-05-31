from flask import Flask, request
import ast  # For safe evaluation

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.args.get('file_contents', '')
    # Extract content between first { and last }
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return {}  # Return empty dict if no valid JSON
    content = file_contents[start+1:end]
    try:
        # Use ast.literal_eval for safer evaluation of the dictionary string
        result_dict = ast.literal_eval(content)
        return app.response_class(str(result_dict), mimetype='application/json')
    except (ValueError, SyntaxError):
        return {}  # Return empty dict on invalid content

# Example usage:
# curl "http://localhost:5000/eval?file_contents=hello%20%7B%20%22key%22%3A%20%22value%22%20%7D%20world"