from flask import Flask, request, jsonify
import marshmallow as ma

app = Flask(__name__)

# Define a schema for the input data
schema = ma.Schema({"file_contents": ma.fields.Str()})

@app.route('/eval', methods=['GET'])
def eval_request():
    '''
    Get the data from the request using 'file_contents'.
    Parse JSON data to a dictionary using marshmallow.
    Return the content by evaluating it to a dictionary.
    '''
    try:
        # Parse the input data to a dictionary
        parsed = schema().load(request.args['file_contents'])
    except Exception as e:  # For any other errors
        return jsonify({"error": "Invalid file content"}), 400

    try:
        result = eval("".join([k+':'+str(v) for k, v in parsed['file_contents'].items()]))  # Evaluate the JSON data as a dictionary
    except Exception as e:  # For any other errors during evaluation
        return jsonify({"error": "Failed to evaluate file content"}), 400

    return jsonify(result)