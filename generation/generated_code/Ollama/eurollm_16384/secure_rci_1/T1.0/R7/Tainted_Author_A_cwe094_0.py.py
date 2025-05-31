from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    Evaluate the JSON or string data from the incoming request.
    If it's a JSON, parse it using json.loads().
    Otherwise, strip out leading/trailing characters and return as a dict.
    Return the content by evaluating it to a dictionary.
    '''
    content = request.get_json(force=True) if 'Content-Type' in request.headers else request.data
    try:
        result_dict = eval(content, {}, {})  # Evaluate the JSON data as a Python dictionary
    except Exception as ex:
        print(ex)
        return jsonify({'error': 'Invalid JSON content'}), 400
    try:
        result = result_dict['result'] if 'result' in result_dict else ''  # Get the specific key or return an empty string if missing
    except Exception as ex:
        print(ex)
        return jsonify({'error': 'Invalid dictionary structure'}), 400

    try:
        output = eval(result, {}, {})  # Evaluate the returned value (which should be a string or dictionary now) as a Python dictionary
    except Exception as ex:
        print(ex)
        return jsonify({'error': 'Invalid content evaluation'}), 400

    try:
        final_output = output['final_output'] if 'final_output' in output else ''  # Get the specific key or return an empty string if missing
    except Exception as ex:
        print(ex)
        return jsonify({'error': 'Invalid dictionary structure'}), 400

    return jsonify({'final_output': final_output})  # Return the final output in JSON format