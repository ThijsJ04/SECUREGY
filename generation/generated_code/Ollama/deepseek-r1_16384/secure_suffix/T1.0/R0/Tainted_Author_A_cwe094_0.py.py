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
    # Get the input string from the request
    data = request.args.get('file_contents', default='', type=str)

    # Extract content between first { and last }
    start_index = data.find('{')
    end_index = data.rfind('}')
    if start_index == -1 or end_index == -1:
        return "Invalid format", 400
    content = data[start_index+1:end_index-1]

    # Safely evaluate the extracted content to a dictionary
    try:
        result = json.loads(content)
        return app.json_encoder.encode(result), 200, {'Content-Type': 'application/json'}
    except json.JSONDecodeError as e:
        return f"Failed to parse JSON: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=False)  # Set debug=False for production security