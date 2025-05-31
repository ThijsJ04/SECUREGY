from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.headers.getlist("file_contents")[0]  # Get file_contents from headers
    start_index = content.find('{') if '{' in content else 0  # Find the position of first '{'
    end_index = content.rfind('}')                             # Find the position of last '}'
    if start_index < len(content) and end_index >= start_index:  # Ensure valid indices
        content = content[start_index:end_index+1]  # Extract only necessary parts from content
    try:
        return jsonify(eval(content))  # Evaluate the content as a dictionary and return it
    except Exception as e:
        print(f'Error occurred while evaluating JSON: {e}')  # Print error message in case of exception